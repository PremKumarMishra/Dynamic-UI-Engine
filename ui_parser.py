from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QPushButton,QSpinBox,QScrollArea,QSlider,QLineEdit,QTabWidget,QComboBox, QCheckBox, QRadioButton, QWidget, QVBoxLayout, QHBoxLayout,QProgressBar,QSpacerItem,QSizePolicy
from PyQt5.QtGui import QFont,QIcon,QPixmap,QPalette,QBrush,QPainter,QColor
from PyQt5.QtCore import QRect,Qt,QTimer,QObject,QEvent,QPropertyAnimation,QVariantAnimation,QAbstractAnimation,QSize

from Helper import HoverHandler,calculateScaleFactor,SCALE_FACTOR
from CustomWidgets.swtich import QSwitch

#Custom Widget For Showing Picture
class ImageFrame(QFrame):
    def __init__(self, image_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_path = image_path

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.image_path)
        painter.drawPixmap(self.rect(), pixmap)
        # super().paintEvent(event)


class DynamicUIParser:
    def __init__(self, ui_data,functions):
        self.ui_data = ui_data
        self.functions = functions

    def parse(self):
        window = DynamicUIWindow(self.ui_data,self.functions)
        return window

class DynamicUIWindow(QMainWindow):
    def __init__(self, ui_data,functions):
        super().__init__()
        self.ui_data = ui_data
        self.functions = functions
        self.widget_registry = {}
        self.initUI()

    def initUI(self):
        #Calculate Scaling Factor
        calculateScaleFactor(1366,768)

        #Set Window Title
        self.setWindowTitle(self.ui_data.get('window_title', 'Dynamic UI with Multiple Widgets'))

        #Set Window Geometry
        geometry = self.ui_data.get('geometry', [100, 100, 600, 400])
        if geometry[0] == "null" and geometry[1] =="null":
            geometry = [round(geom*SCALE_FACTOR) for geom in geometry[2:]]
            self.setFixedSize(*geometry)
        else:
            geometry = [round(geom*SCALE_FACTOR) for geom in geometry]
            self.setGeometry(*geometry)

        # Apply the main window stylesheet if provided
        window_stylesheet = self.ui_data.get('stylesheet', '')
        if window_stylesheet:
            self.setStyleSheet(window_stylesheet)

        #Apply Main Window Icon if provided
        window_icon =  self.ui_data.get('icon',None)
        self.setWindowIcon(QIcon(window_icon))

        #Apply Main Window Flags if provided
        window_flag = self.ui_data.get("flags")
        if window_flag:
            window_flag = self.getWindowTypeByName(window_flag)
            if window_flag:
                self.setWindowFlags(window_flag)
        
        #Apply Main Window Attributes if provided
        window_attribute = self.ui_data.get("attribute")
        if window_attribute:
            window_attribute = self.getWidgetAttributeByName(window_attribute)
            if window_attribute:
                self.setAttribute(window_attribute)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout_data = self.ui_data.get('layout')
        if layout_data:
            main_layout = self.create_layout(layout_data)
            main_widget.setLayout(main_layout)

    def create_layout(self, layout_data):
        layout_type = layout_data.get('type')
        layout_margin =  layout_data.get('margin')
        layout_spacing = layout_data.get('spacing')
        layout_alignment = layout_data.get('alignment')

        if layout_type == 'vertical':
            layout = QVBoxLayout()
        elif layout_type == 'horizontal':
            layout = QHBoxLayout()
        else:
            layout = QVBoxLayout()  # Default to vertical layout if unspecified
        
        if layout_margin:
            layout_margin = [round(margin*SCALE_FACTOR) for margin in layout_margin]
            layout.setContentsMargins(*layout_margin)
        if layout_spacing or isinstance(layout_spacing,int):
            layout.setSpacing(round(layout_spacing*SCALE_FACTOR))
        if layout_alignment:
            layout_alignment = eval(layout_alignment)
            layout.setAlignment(layout_alignment)
            

        for widget_data in layout_data.get('widgets', []):
            if 'type' in widget_data and widget_data['type'] in ['vertical', 'horizontal']:
                nested_layout = self.create_layout(widget_data)
                layout.addLayout(nested_layout)
            else:
                widget = self.create_widget(widget_data)
                if widget and not isinstance(widget,(QTimer,QSpacerItem)):
                    widget_anchor = widget_data.get('anchor')
                    if widget_anchor:
                        widget_anchor = self.getAlignmentByName(widget_anchor)
                        if widget_anchor:
                            layout.addWidget(widget,alignment=widget_anchor)
                    else:
                        layout.addWidget(widget)
                else:
                    if widget and isinstance(widget,QSpacerItem):
                        layout.addSpacerItem(widget)
        return layout
    
    #Set Background Image To Any Widget
    def setBackgroundImage(self,widget,pixmap):
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        widget.setAutoFillBackground(True)
        widget.setPalette(palette)
    
    #Get Alignment By UI String Property
    def getAlignmentByName(self,anchor):
        match anchor:
            case "left":
                return Qt.AlignmentFlag.AlignLeft
            case "right":
                return Qt.AlignmentFlag.AlignRight
            case "top":
                return Qt.AlignmentFlag.AlignTop
            case "bottom":
                return Qt.AlignmentFlag.AlignBottom
            case "center":
                return Qt.AlignmentFlag.AlignCenter
            case "absolute":
                return Qt.AlignmentFlag.AlignAbsolute
            case "justify":
                return Qt.AlignmentFlag.AlignJustify
            case "hcenter":
                return Qt.AlignmentFlag.AlignHCenter
            case "vcenter":
                return Qt.AlignmentFlag.AlignVCenter
            case "baseline":
                return Qt.AlignmentFlag.AlignBaseline
            case "trailing":
                return Qt.AlignmentFlag.AlignTrailing
            case "leading":
                return Qt.AlignmentFlag.AlignLeading
            case "horizontal_mask":
                return Qt.AlignmentFlag.AlignHorizontal_Mask
            case "vertical_mask":
                return Qt.AlignmentFlag.AlignVertical_Mask
            

    #Get Cursor Shape By UI String Property
    def getCursorShapeByName(self,shape):
        match shape:
            case 'ArrowCursor':
                return Qt.CursorShape.ArrowCursor
            case 'BitmapCursor':
                return Qt.CursorShape.BitmapCursor
            case 'BlankCursor':
                return Qt.CursorShape.BlankCursor
            case 'BusyCursor':
                return Qt.CursorShape.BusyCursor
            case 'ClosedHandCursor':
                return Qt.CursorShape.ClosedHandCursor
            case 'CustomCursor':
                return Qt.CursorShape.CustomCursor
            case 'DragCopyCursor':
                return Qt.CursorShape.DragCopyCursor
            case 'DragLinkCursor':
                return Qt.CursorShape.DragLinkCursor
            case 'DragMoveCursor':
                return Qt.CursorShape.DragMoveCursor
            case 'ForbiddenCursor':
                return Qt.CursorShape.ForbiddenCursor
            case 'IBeamCursor':
                return Qt.CursorShape.IBeamCursor
            case 'LastCursor':
                return Qt.CursorShape.LastCursor
            case 'OpenHandCursor':
                return Qt.CursorShape.OpenHandCursor
            case 'PointingHandCursor':
                return Qt.CursorShape.PointingHandCursor
            case 'SizeAllCursor':
                return Qt.CursorShape.SizeAllCursor
            case 'SizeBDiagCursor':
                return Qt.CursorShape.SizeBDiagCursor
            case 'SizeHorCursor':
                return Qt.CursorShape.SizeHorCursor
            case 'SizeVerCursor':
                return Qt.CursorShape.SizeVerCursor
            case 'SplitHCursor':
                return Qt.CursorShape.SplitHCursor
            case 'SplitVCursor':
                return Qt.CursorShape.SplitVCursor
            case 'UpArrowCursor':
                return Qt.CursorShape.UpArrowCursor
            case 'WaitCursor':
                return Qt.CursorShape.WaitCursor
            case 'WhatsThisCursor':
                return Qt.CursorShape.WhatsThisCursor
    
    # Get Window Type By Name
    def getWindowTypeByName(self, type):
        match type:
            case 'BypassGraphicsProxyWidget':
                return Qt.WindowType.BypassGraphicsProxyWidget
            case 'BypassWindowManagerHint':
                return Qt.WindowType.BypassWindowManagerHint
            case 'CoverWindow':
                return Qt.WindowType.CoverWindow
            case 'CustomizeWindowHint':
                return Qt.WindowType.CustomizeWindowHint
            case 'Desktop':
                return Qt.WindowType.Desktop
            case 'Dialog':
                return Qt.WindowType.Dialog
            case 'Drawer':
                return Qt.WindowType.Drawer
            case 'ForeignWindow':
                return Qt.WindowType.ForeignWindow
            case 'FramelessWindowHint':
                return Qt.WindowType.FramelessWindowHint
            case 'MacWindowToolBarButtonHint':
                return Qt.WindowType.MacWindowToolBarButtonHint
            case 'MaximizeUsingFullscreenGeometryHint':
                return Qt.WindowType.MaximizeUsingFullscreenGeometryHint
            case 'MSWindowsFixedSizeDialogHint':
                return Qt.WindowType.MSWindowsFixedSizeDialogHint
            case 'MSWindowsOwnDC':
                return Qt.WindowType.MSWindowsOwnDC
            case 'NoDropShadowWindowHint':
                return Qt.WindowType.NoDropShadowWindowHint
            case 'Popup':
                return Qt.WindowType.Popup
            case 'Sheet':
                return Qt.WindowType.Sheet
            case 'SplashScreen':
                return Qt.WindowType.SplashScreen
            case 'SubWindow':
                return Qt.WindowType.SubWindow
            case 'Tool':
                return Qt.WindowType.Tool
            case 'ToolTip':
                return Qt.WindowType.ToolTip
            case 'Widget':
                return Qt.WindowType.Widget
            case 'Window':
                return Qt.WindowType.Window
            case 'WindowCloseButtonHint':
                return Qt.WindowType.WindowCloseButtonHint
            case 'WindowContextHelpButtonHint':
                return Qt.WindowType.WindowContextHelpButtonHint
            case 'WindowDoesNotAcceptFocus':
                return Qt.WindowType.WindowDoesNotAcceptFocus
            case 'WindowFullscreenButtonHint':
                return Qt.WindowType.WindowFullscreenButtonHint
            case 'WindowMaximizeButtonHint':
                return Qt.WindowType.WindowMaximizeButtonHint
            case 'WindowMinMaxButtonsHint':
                return Qt.WindowType.WindowMinMaxButtonsHint
            case 'WindowOverridesSystemGestures':
                return Qt.WindowType.WindowOverridesSystemGestures
            case 'WindowShadeButtonHint':
                return Qt.WindowType.WindowShadeButtonHint
            case 'WindowStaysOnBottomHint':
                return Qt.WindowType.WindowStaysOnBottomHint
            case 'WindowStaysOnTopHint':
                return Qt.WindowType.WindowStaysOnTopHint
            case 'WindowSystemMenuHint':
                return Qt.WindowType.WindowSystemMenuHint
            case 'WindowTitleHint':
                return Qt.WindowType.WindowTitleHint
            case 'WindowTransparentForInput':
                return Qt.WindowType.WindowTransparentForInput
            case 'WindowType_Mask':
                return Qt.WindowType.WindowType_Mask
            case 'X11BypassWindowManagerHint':
                return Qt.WindowType.X11BypassWindowManagerHint
    
    #Get Widget Attribute By Name
    def getWidgetAttributeByName(self, widAttr):
        match widAttr:
            case 'WA_AcceptDrops':
                return Qt.WidgetAttribute.WA_AcceptDrops
            case 'WA_AlwaysShowToolTips':
                return Qt.WidgetAttribute.WA_AlwaysShowToolTips
            case 'WA_AcceptTouchEvents':
                return Qt.WidgetAttribute.WA_AcceptTouchEvents
            case 'WA_AlwaysStackOnTop':
                return Qt.WidgetAttribute.WA_AlwaysStackOnTop
            case 'WA_AttributeCount':
                return Qt.WidgetAttribute.WA_AttributeCount
            case 'WA_ContentsMarginsRespectsSafeArea':
                return Qt.WidgetAttribute.WA_ContentsMarginsRespectsSafeArea
            case 'WA_CustomWhatsThis':
                return Qt.WidgetAttribute.WA_CustomWhatsThis
            case 'WA_DeleteOnClose':
                return Qt.WidgetAttribute.WA_DeleteOnClose
            case 'WA_Disabled':
                return Qt.WidgetAttribute.WA_Disabled
            case 'WA_DontCreateNativeAncestors':
                return Qt.WidgetAttribute.WA_DontCreateNativeAncestors
            case 'WA_DontShowOnScreen':
                return Qt.WidgetAttribute.WA_DontShowOnScreen
            case 'WA_ForceDisabled':
                return Qt.WidgetAttribute.WA_ForceDisabled
            case 'WA_ForceUpdatesDisabled':
                return Qt.WidgetAttribute.WA_ForceUpdatesDisabled
            case 'WA_GrabbedShortcut':
                return Qt.WidgetAttribute.WA_GrabbedShortcut
            case 'WA_GroupLeader':
                return Qt.WidgetAttribute.WA_GroupLeader
            case 'WA_Hover':
                return Qt.WidgetAttribute.WA_Hover
            case 'WA_InputMethodEnabled':
                return Qt.WidgetAttribute.WA_InputMethodEnabled
            case 'WA_InputMethodTransparent':
                return Qt.WidgetAttribute.WA_InputMethodTransparent
            case 'WA_InvalidSize':
                return Qt.WidgetAttribute.WA_InvalidSize
            case 'WA_KeyboardFocusChange':
                return Qt.WidgetAttribute.WA_KeyboardFocusChange
            case 'WA_KeyCompression':
                return Qt.WidgetAttribute.WA_KeyCompression
            case 'WA_LaidOut':
                return Qt.WidgetAttribute.WA_LaidOut
            case 'WA_LayoutOnEntireRect':
                return Qt.WidgetAttribute.WA_LayoutOnEntireRect
            case 'WA_LayoutUsesWidgetRect':
                return Qt.WidgetAttribute.WA_LayoutUsesWidgetRect
            case 'WA_MacAlwaysShowToolWindow':
                return Qt.WidgetAttribute.WA_MacAlwaysShowToolWindow
            case 'WA_MacBrushedMetal':
                return Qt.WidgetAttribute.WA_MacBrushedMetal
            case 'WA_MacFrameworkScaled':
                return Qt.WidgetAttribute.WA_MacFrameworkScaled
            case 'WA_MacMetalStyle':
                return Qt.WidgetAttribute.WA_MacMetalStyle
            case 'WA_MacMiniSize':
                return Qt.WidgetAttribute.WA_MacMiniSize
            case 'WA_MacNoClickThrough':
                return Qt.WidgetAttribute.WA_MacNoClickThrough
            case 'WA_MacNormalSize':
                return Qt.WidgetAttribute.WA_MacNormalSize
            case 'WA_MacNoShadow':
                return Qt.WidgetAttribute.WA_MacNoShadow
            case 'WA_MacOpaqueSizeGrip':
                return Qt.WidgetAttribute.WA_MacOpaqueSizeGrip
            case 'WA_MacShowFocusRect':
                return Qt.WidgetAttribute.WA_MacShowFocusRect
            case 'WA_MacSmallSize':
                return Qt.WidgetAttribute.WA_MacSmallSize
            case 'WA_MacVariableSize':
                return Qt.WidgetAttribute.WA_MacVariableSize
            case 'WA_Mapped':
                return Qt.WidgetAttribute.WA_Mapped
            case 'WA_MouseNoMask':
                return Qt.WidgetAttribute.WA_MouseNoMask
            case 'WA_MouseTracking':
                return Qt.WidgetAttribute.WA_MouseTracking
            case 'WA_Moved':
                return Qt.WidgetAttribute.WA_Moved
            case 'WA_MSWindowsUseDirect3D':
                return Qt.WidgetAttribute.WA_MSWindowsUseDirect3D
            case 'WA_NativeWindow':
                return Qt.WidgetAttribute.WA_NativeWindow
            case 'WA_NoChildEventsForParent':
                return Qt.WidgetAttribute.WA_NoChildEventsForParent
            case 'WA_NoChildEventsFromChildren':
                return Qt.WidgetAttribute.WA_NoChildEventsFromChildren
            case 'WA_NoMousePropagation':
                return Qt.WidgetAttribute.WA_NoMousePropagation
            case 'WA_NoMouseReplay':
                return Qt.WidgetAttribute.WA_NoMouseReplay
            case 'WA_NoSystemBackground':
                return Qt.WidgetAttribute.WA_NoSystemBackground
            case 'WA_NoX11EventCompression':
                return Qt.WidgetAttribute.WA_NoX11EventCompression
            case 'WA_OpaquePaintEvent':
                return Qt.WidgetAttribute.WA_OpaquePaintEvent
            case 'WA_OutsideWSRange':
                return Qt.WidgetAttribute.WA_OutsideWSRange
            case 'WA_PaintOnScreen':
                return Qt.WidgetAttribute.WA_PaintOnScreen
            case 'WA_PaintUnclipped':
                return Qt.WidgetAttribute.WA_PaintUnclipped
            case 'WA_PendingMoveEvent':
                return Qt.WidgetAttribute.WA_PendingMoveEvent
            case 'WA_PendingResizeEvent':
                return Qt.WidgetAttribute.WA_PendingResizeEvent
            case 'WA_PendingUpdate':
                return Qt.WidgetAttribute.WA_PendingUpdate
            case 'WA_QuitOnClose':
                return Qt.WidgetAttribute.WA_QuitOnClose
            case 'WA_Resized':
                return Qt.WidgetAttribute.WA_Resized
            case 'WA_RightToLeft':
                return Qt.WidgetAttribute.WA_RightToLeft
            case 'WA_SetCursor':
                return Qt.WidgetAttribute.WA_SetCursor
            case 'WA_SetFont':
                return Qt.WidgetAttribute.WA_SetFont
            case 'WA_SetLayoutDirection':
                return Qt.WidgetAttribute.WA_SetLayoutDirection
            case 'WA_SetLocale':
                return Qt.WidgetAttribute.WA_SetLocale
            case 'WA_SetPalette':
                return Qt.WidgetAttribute.WA_SetPalette
            case 'WA_SetStyle':
                return Qt.WidgetAttribute.WA_SetStyle
            case 'WA_SetWindowIcon':
                return Qt.WidgetAttribute.WA_SetWindowIcon
            case 'WA_ShowWithoutActivating':
                return Qt.WidgetAttribute.WA_ShowWithoutActivating
            case 'WA_StaticContents':
                return Qt.WidgetAttribute.WA_StaticContents
            case 'WA_StyledBackground':
                return Qt.WidgetAttribute.WA_StyledBackground
            case 'WA_StyleSheet':
                return Qt.WidgetAttribute.WA_StyleSheet
            case 'WA_StyleSheetTarget':
                return Qt.WidgetAttribute.WA_StyleSheetTarget
            case 'WA_TabletTracking':
                return Qt.WidgetAttribute.WA_TabletTracking
            case 'WA_TintedBackground':
                return Qt.WidgetAttribute.WA_TintedBackground
            case 'WA_TouchPadAcceptSingleTouchEvents':
                return Qt.WidgetAttribute.WA_TouchPadAcceptSingleTouchEvents
            case 'WA_TranslucentBackground':
                return Qt.WidgetAttribute.WA_TranslucentBackground
            case 'WA_TransparentForMouseEvents':
                return Qt.WidgetAttribute.WA_TransparentForMouseEvents
            case 'WA_UnderMouse':
                return Qt.WidgetAttribute.WA_UnderMouse
            case 'WA_UpdatesDisabled':
                return Qt.WidgetAttribute.WA_UpdatesDisabled
            case 'WA_WindowModified':
                return Qt.WidgetAttribute.WA_WindowModified
            case 'WA_WindowPropagation':
                return Qt.WidgetAttribute.WA_WindowPropagation
            case 'WA_WState_CompressKeys':
                return Qt.WidgetAttribute.WA_WState_CompressKeys
            case 'WA_WState_ExplicitShowHide':
                return Qt.WidgetAttribute.WA_WState_ExplicitShowHide
            case 'WA_WState_ConfigPending':
                return Qt.WidgetAttribute.WA_WState_ConfigPending
            case 'WA_WState_Created':
                return Qt.WidgetAttribute.WA_WState_Created
            case 'WA_WState_Hidden':
                return Qt.WidgetAttribute.WA_WState_Hidden
            case 'WA_WState_InPaintEvent':
                return Qt.WidgetAttribute.WA_WState_InPaintEvent
            case 'WA_WState_Reparented':
                return Qt.WidgetAttribute.WA_WState_Reparented
            case 'WA_WState_OwnSizePolicy':
                return Qt.WidgetAttribute.WA_WState_OwnSizePolicy
            case 'WA_WState_Polished':
                return Qt.WidgetAttribute.WA_WState_Polished
            case 'WA_WState_Visible':
                return Qt.WidgetAttribute.WA_WState_Visible
            case 'WA_X11DoNotAcceptFocus':
                return Qt.WidgetAttribute.WA_X11DoNotAcceptFocus
            case 'WA_X11NetWmWindowTypeCombo':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeCombo
            case 'WA_X11NetWmWindowTypeDesktop':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeDesktop
            case 'WA_X11NetWmWindowTypeDialog':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeDialog
            case 'WA_X11NetWmWindowTypeDND':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeDND
            case 'WA_X11NetWmWindowTypeDock':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeDock
            case 'WA_X11NetWmWindowTypeDropDownMenu':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeDropDownMenu
            case 'WA_X11NetWmWindowTypeMenu':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeMenu
            case 'WA_X11NetWmWindowTypeNotification':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeNotification
            case 'WA_X11NetWmWindowTypePopupMenu':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypePopupMenu
            case 'WA_X11NetWmWindowTypeSplash':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeSplash
            case 'WA_X11NetWmWindowTypeToolBar':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeToolBar
            case 'WA_X11NetWmWindowTypeToolTip':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeToolTip
            case 'WA_X11NetWmWindowTypeUtility':
                return Qt.WidgetAttribute.WA_X11NetWmWindowTypeUtility
            case 'WA_X11OpenGLOverlay':
                return Qt.WidgetAttribute.WA_X11OpenGLOverlay

    # Get Color Role By Name
    def getColorRoleByName(self, colorRole):
        match colorRole:
            case 'Background':
                return QPalette.ColorRole.Background
            case 'Base':
                return QPalette.ColorRole.Base
            case 'BrightText':
                return QPalette.ColorRole.BrightText
            case 'Button':
                return QPalette.ColorRole.Button
            case 'AlternateBase':
                return QPalette.ColorRole.AlternateBase
            case 'Dark':
                return QPalette.ColorRole.Dark
            case 'Foreground':
                return QPalette.ColorRole.Foreground
            case 'Highlight':
                return QPalette.ColorRole.Highlight
            case 'HighlightedText':
                return QPalette.ColorRole.HighlightedText
            case 'Light':
                return QPalette.ColorRole.Light
            case 'Link':
                return QPalette.ColorRole.Link
            case 'LinkVisited':
                return QPalette.ColorRole.LinkVisited
            case 'Mid':
                return QPalette.ColorRole.Mid
            case 'Midlight':
                return QPalette.ColorRole.Midlight
            case 'NColorRoles':
                return QPalette.ColorRole.NColorRoles
            case 'NoRole':
                return QPalette.ColorRole.NoRole
            case 'PlaceholderText':
                return QPalette.ColorRole.PlaceholderText
            case 'Shadow':
                return QPalette.ColorRole.Shadow
            case 'Text':
                return QPalette.ColorRole.Text
            case 'ToolTipBase':
                return QPalette.ColorRole.ToolTipBase
            case 'BrightText':
                return QPalette.ColorRole.BrightText
            case 'Window':
                return QPalette.ColorRole.Window
            case 'WindowText':
                return QPalette.ColorRole.WindowText
            

    # Get Focus Reason By Name
    def getFocusReasonByName(self, focus):
        match focus:
            case 'BacktabFocusReason':
                return Qt.FocusReason.BacktabFocusReason
            case 'ActiveWindowFocusReason':
                return Qt.FocusReason.ActiveWindowFocusReason
            case 'MenuBarFocusReason':
                return Qt.FocusReason.MenuBarFocusReason
            case 'MouseFocusReason':
                return Qt.FocusReason.MouseFocusReason
            case 'NoFocusReason':
                return Qt.FocusReason.NoFocusReason
            case 'OtherFocusReason':
                return Qt.FocusReason.OtherFocusReason
            case 'PopupFocusReason':
                return Qt.FocusReason.PopupFocusReason
            case 'ShortcutFocusReason':
                return Qt.FocusReason.ShortcutFocusReason
            case 'TabFocusReason':
                return Qt.FocusReason.TabFocusReason

    # Get Focus Policy By Name
    def getFocusPolicyByName(self, fPolicy):
        match fPolicy:
            case 'ClickFocus':
                return Qt.FocusPolicy.ClickFocus
            case 'NoFocus':
                return Qt.FocusPolicy.NoFocus
            case 'StrongFocus':
                return Qt.FocusPolicy.StrongFocus
            case 'TabFocus':
                return Qt.FocusPolicy.TabFocus
            case 'WheelFocus':
                return Qt.FocusPolicy.WheelFocus

    # Get Orientation By Name
    def getOrientationByName(self, orientation):
        match orientation:
            case 'Horizontal':
                return Qt.Orientation.Horizontal
            case 'Vertical':
                return Qt.Orientation.Vertical
            

    # Get Scroll Bar Policy By Name
    def getScrollBarPolicyByName(self, sbPolicy):
        match sbPolicy:
            case 'ScrollBarAlwaysOff':
                return Qt.ScrollBarPolicy.ScrollBarAlwaysOff
            case 'ScrollBarAlwaysOn':
                return Qt.ScrollBarPolicy.ScrollBarAlwaysOn
            case 'ScrollBarAsNeeded':
                return Qt.ScrollBarPolicy.ScrollBarAsNeeded

    # Get Text In teraction Flag By Name
    def getTextInteractionFlagByName(self, flag):
        match flag:
            case 'LinksAccessibleByKeyboard':
                return Qt.TextInteractionFlag.LinksAccessibleByKeyboard
            case 'LinksAccessibleByMouse':
                return Qt.TextInteractionFlag.LinksAccessibleByMouse
            case 'NoTextInteraction':
                return Qt.TextInteractionFlag.NoTextInteraction
            case 'TextBrowserInteraction':
                return Qt.TextInteractionFlag.TextBrowserInteraction
            case 'TextEditable':
                return Qt.TextInteractionFlag.TextEditable
            case 'TextEditorInteraction':
                return Qt.TextInteractionFlag.TextEditorInteraction
            case 'TextSelectableByKeyboard':
                return Qt.TextInteractionFlag.TextSelectableByKeyboard
            case 'TextSelectableByMouse':
                return Qt.TextInteractionFlag.TextSelectableByMouse


    ##Get Size Policy By UI String Property   
    def getSizePolicyByName(self,policy):
        match policy:
            case "expanding":
                return QSizePolicy.Policy.Expanding
            case "fixed":
                return QSizePolicy.Policy.Fixed
            case "minimum":
                return QSizePolicy.Policy.Minimum
            case "maximum":
                return QSizePolicy.Policy.Maximum
            case "preferred":
                return QSizePolicy.Policy.Preferred
            case "ignored":
                return QSizePolicy.Policy.Ignored
            case "minimum_expanding":
                return QSizePolicy.Policy.MinimumExpanding

    #Apply Animation To Widgets
    def applyAnimation(self, widget, animation_data):
        trigger = animation_data.get('trigger')
        if trigger == 'hover':
            hover_handler = HoverHandler(widget, animation_data)
            widget.installEventFilter(hover_handler)

    #Create Widgets According To JSON Data      
    def create_widget(self, widget_data):
        widget_type = widget_data.get('type')
        if widget_type == 'label':
            widget = self.create_label(widget_data)
        elif widget_type == 'frame':
            widget = self.create_frame(widget_data)
        elif widget_type == 'button':
            widget = self.create_button(widget_data)
        elif widget_type == 'lineedit':
            widget = self.create_lineedit(widget_data)
        elif widget_type == 'combobox':
            widget = self.create_combobox(widget_data)
        elif widget_type == 'checkbox':
            widget = self.create_checkbox(widget_data)
        elif widget_type == 'radiobutton':
            widget = self.create_radiobutton(widget_data)
        elif widget_type == 'progressbar':
            widget = self.create_progressbar(widget_data)
        elif widget_type == 'tabwidget':
            widget = self.create_tabwidget(widget_data)
        elif widget_type == 'scrollarea':
            widget = self.create_scrollarea(widget_data)
        elif widget_type == 'slider':
            widget = self.create_slider(widget_data)
        elif widget_type == 'spinbox':
            widget = self.create_spinbox(widget_data)
        elif widget_type == 'picture':
            widget = self.create_picture(widget_data)
        elif widget_type == "switch":
            widget = self.create_switch(widget_data)
        elif widget_type == 'timer':
            widget = self.create_timer(widget_data)
        elif widget_type == 'spacerItem':
            widget = self.create_spacerItem(widget_data)
        else:
            widget = None

        if widget and 'id' in widget_data:
            self.widget_registry[widget_data['id']] = widget

        return widget

    def apply_common_properties(self, widget, widget_data):
        # Apply stylesheet if provided
        stylesheet = widget_data.get('stylesheet', '')
        if stylesheet:
            widget.setStyleSheet(stylesheet)
        
        # Apply enabled/disabled state if provided
        enabled = widget_data.get('enabled', True)
        widget.setEnabled(enabled)

        # Apply font if provided
        font_data = widget_data.get('font')
        if font_data:
            font = QFont()
            font.setFamily(font_data.get('family', ''))
            font.setPointSize(round(font_data.get('size', 12)*SCALE_FACTOR))
            font.setBold(font_data.get('bold', False))
            font.setItalic(font_data.get('italic', False))
            widget.setFont(font)

        # Apply Alignments if provided
        alignment = widget_data.get('alignment','')
        if alignment:
            alignment = eval(alignment)
            widget.setAlignment(alignment)

        # Apply Cursor Shape if provided
        cursor = widget_data.get('cursor')
        if cursor:
            cursor = self.getCursorShapeByName(cursor)
            if cursor:
                widget.setCursor(cursor)
                
        #Apply Visibility if provided
        visibility = widget_data.get('visible',True)
        if not visibility:
            widget.hide()

        #Apply Width if provided
        width = widget_data.get('width')
        if width:
            widget.setFixedWidth(round(width*SCALE_FACTOR))
        
        #Apply Height if provided
        height = widget_data.get('height')
        if height:
            widget.setFixedHeight(round(height*SCALE_FACTOR))

        #Apply Minimum Width if provided
        width = widget_data.get('min_width')
        if width:
            widget.setMinimumWidth(round(width*SCALE_FACTOR))

        #Apply Minimum Height if provided
        height = widget_data.get('min_height')
        if height:
            widget.setMinimumHeight(round(height*SCALE_FACTOR))

        #Apply Maximum Width if provided
        width = widget_data.get('max_width')
        if width:
            widget.setMaximumWidth(round(width*SCALE_FACTOR))

        #Apply Maximum Height if provided
        height = widget_data.get('max_height')
        if height:
            widget.setMaximumHeight(round(height*SCALE_FACTOR))
        
        # Apply animation if provided
        animation_data = widget_data.get('animation')
        if animation_data:
            self.applyAnimation(widget, animation_data)

        
    def create_label(self, widget_data):
        label = QLabel(widget_data.get('text', ''))
        self.apply_common_properties(label, widget_data)
        
        #Set Text Interaction Flag If Provided
        interactionFlag = widget_data.get('interaction')
        if interactionFlag:
            interactionFlag = self.getTextInteractionFlagByName(interactionFlag)
            if interactionFlag:
                label.setTextInteractionFlags(interactionFlag)

        #Allow External Links To Open if Provided
        allowExternalLink = widget_data.get('open_external_links',False)       
        label.setOpenExternalLinks(allowExternalLink)

        #Set Pixmap If Provided
        pixmap = widget_data.get('image')
        scale_x = widget_data.get('img-width')
        scale_y = widget_data.get('img-height')
        if isinstance(pixmap,str):
            pixmap = QPixmap(pixmap)
            if scale_x:
                pixmap = pixmap.scaled(round(scale_x*SCALE_FACTOR),pixmap.height(),0,1)
            if scale_y:
                pixmap = pixmap.scaled(pixmap.width(),round(scale_y*SCALE_FACTOR),0,1)
            label.setPixmap(pixmap)
            
        return label
    
    def create_frame(self,widget_data):
        frame = QFrame()
        self.apply_common_properties(frame,widget_data)
        layout_data = widget_data.get('layout')
        if layout_data:
            frame_layout = self.create_layout(layout_data)
            frame.setLayout(frame_layout)

        pixmap = widget_data.get('image')
        scale_x = widget_data.get('img-width')
        scale_y = widget_data.get('img-height')
        if pixmap:
            pixmap = QPixmap(pixmap)
            if scale_x:
                pixmap = pixmap.scaled(scale_x,pixmap.height(),0,1)
            if scale_y:
                pixmap = pixmap.scaled(pixmap.width(),scale_y,0,1)
            self.setBackgroundImage(frame,pixmap)
        
        return frame

    def create_button(self, widget_data):
        button = QPushButton(widget_data.get('text', ''))
        self.apply_common_properties(button, widget_data)

        function_name = widget_data.get('function')
        if function_name:
            function = self.functions.get(function_name)
            if function:
                button.clicked.connect(function)

        checkable = widget_data.get('checkable',False)
        button.setCheckable(checkable)

        checked = widget_data.get('checked',False)
        button.setChecked(checked)

        icon_size = widget_data.get('icon_size')
        if icon_size:
            icon_size = [round(sz*SCALE_FACTOR) for sz in icon_size]
            button.setIconSize(QSize(*icon_size))

        icon = widget_data.get('icon')
        if icon:
            icon = QIcon(icon)
            button.setIcon(icon)

        return button

    def create_lineedit(self, widget_data):
        lineedit = QLineEdit()
        lineedit.setPlaceholderText(widget_data.get('placeholder', ''))
        self.apply_common_properties(lineedit, widget_data)
        
        # Apply read-only state if provided
        read_only = widget_data.get('read_only', False)
        lineedit.setReadOnly(read_only)

        #Set Text If Provided
        text = widget_data.get('text','')
        lineedit.setText(text)
        
        return lineedit

    def create_combobox(self, widget_data):
        combobox = QComboBox()
        items = widget_data.get('items', [])
        combobox.addItems(items)
        self.apply_common_properties(combobox, widget_data)
        return combobox

    def create_checkbox(self, widget_data):
        checkbox = QCheckBox(widget_data.get('text', ''))
        self.apply_common_properties(checkbox, widget_data)
        return checkbox

    def create_radiobutton(self, widget_data):
        radiobutton = QRadioButton(widget_data.get('text', ''))
        self.apply_common_properties(radiobutton, widget_data)
        return radiobutton
    
    def create_progressbar(self, widget_data):
        progressbar = QProgressBar()
        progressbar.setFormat(widget_data.get('text', ''))
        progressbar.setValue(widget_data.get('value', 0))
        progressbar.setTextVisible(widget_data.get('text-visible', True))
        self.apply_common_properties(progressbar, widget_data)
        return progressbar
    
    def create_tabwidget(self, widget_data):
        tab_widget = QTabWidget()
        self.apply_common_properties(tab_widget, widget_data)

        for tab_data in widget_data.get('tabs', []):
            tab_title = tab_data.get('title', 'Tab')
            tab_content = self.create_widget({
                'type': 'frame',
                'layout': tab_data.get('layout', {})
            })
            tab_widget.addTab(tab_content, tab_title)

        return tab_widget
    
    def create_scrollarea(self, widget_data):
        scroll_area = QScrollArea()
        self.apply_common_properties(scroll_area, widget_data)

        resizable = widget_data.get('resizable',True)
        scroll_area.setWidgetResizable(resizable)

        # Apply vertical scrollbar policy if provided
        vscrollbarPolicy = widget_data.get('vscrollbarpolicy')
        if vscrollbarPolicy:
            vscrollbarPolicy = self.getScrollBarPolicyByName(vscrollbarPolicy)
            if vscrollbarPolicy:
                scroll_area.setVerticalScrollBarPolicy(vscrollbarPolicy)
        
        # Apply horizontal scrollbar policy if provided
        hscrollbarPolicy = widget_data.get('hscrollbarpolicy')
        if hscrollbarPolicy:
            hscrollbarPolicy = self.getScrollBarPolicyByName(hscrollbarPolicy)
            if hscrollbarPolicy:
                scroll_area.setHorizontalScrollBarPolicy(hscrollbarPolicy)

        #Set Scrollbar Widget Data
        widget_data = widget_data.get('widget')
        if widget_data:
            widget = self.create_widget(widget_data)
            scroll_area.setWidget(widget)

        return scroll_area

    def create_slider(self,widget_data):
        slider = QSlider()
        self.apply_common_properties(slider,widget_data)
       
       #Apply Orientation if provided
        orientation = widget_data.get('orientation')
        if orientation:
            orientation = self.getOrientationByName(orientation)
            if orientation:
                slider.setOrientation(orientation)
        
        #Apply Range if provided
        Range = widget_data.get('range')
        if Range:
            slider.setRange(*Range)

        #Set Value If Provided
        value = widget_data.get('value',0)
        slider.setValue(value)
                
        return slider
    
    def create_spinbox(self,widget_data):
        spinbox = QSpinBox()
        self.apply_common_properties(spinbox,widget_data)

        # Apply read-only state if provided
        read_only = widget_data.get('read_only', False)
        spinbox.setReadOnly(read_only)

        #Apply Range if provided
        Range = widget_data.get('range')
        if Range:
            spinbox.setRange(*Range)

        #Set Value If Provided
        value = widget_data.get('value',0)
        spinbox.setValue(value)

        return spinbox
    
    def create_picture(self,widget_data):
        pixmap = widget_data.get('image',QPixmap)
        if isinstance(pixmap,str):
            pixmap = QPixmap(pixmap)
        picture = ImageFrame(pixmap)
        self.apply_common_properties(picture,widget_data)
        layout_data = widget_data.get('layout')
        if layout_data:
            frame_layout = self.create_layout(layout_data)
            picture.setLayout(frame_layout)
        return picture
    
    def create_switch(self,widget_data):
        switch = QSwitch()
        self.apply_common_properties(switch,widget_data)

        checked = widget_data.get('checked',False)
        switch.setChecked(checked)

        return switch
    
    def create_timer(self,widget_data):
        timer = QTimer()
        timer.setSingleShot(widget_data.get('singleshot', False))
        timer.setInterval(widget_data.get('interval', 1000))
        function_name = widget_data.get('function')
        if function_name:
            function = self.functions.get(function_name)
            if function:
                timer.timeout.connect(function)
        timer.start()
        return timer
    
    def create_spacerItem(self,widget_data):
        width = round(widget_data.get('width',0)*SCALE_FACTOR)
        height = round(widget_data.get('height',0)*SCALE_FACTOR)
        hPolicy = widget_data.get('hpolicy',QSizePolicy.Policy.Expanding)
        vPolicy = widget_data.get('vpolicy',QSizePolicy.Policy.Expanding)
        if isinstance(hPolicy,str):
            hPolicy = self.getSizePolicyByName(hPolicy)
        if isinstance(vPolicy,str):
            vPolicy = self.getSizePolicyByName(vPolicy)
        
        return QSpacerItem(width,height,hPolicy,vPolicy)    


    def find_widget_by_id(self, widget_id):
        return self.widget_registry.get(widget_id)

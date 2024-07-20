import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from ui_parser import DynamicUIParser

def go_to_page_1():
    print("Navigated to Page 1")

def go_to_page_2():
    print("Navigated to Page 2")

def printf():
    print("hello")
    # window.find_widget_by_id("timer1").stop()

def load_ui_data():
    ui_data_json = '''
    {
        "window_title" : "Launcher Settings",
        "geometry" : ["null","null",405, 370],
        "flags" : "WindowCloseButtonHint",
        "stylesheet" : "font-family : 'Century Gothic';font-weight:bold;font-size:13px;",
        "layout" : {
            "type" : "vertical",
            "margin" : [0,0,0,0],
            "spacing" : 0,

            "widgets" : [
                {
                    "type" : "picture",
                    "image" : "C:/Users/Prem/Desktop/t/igin.png",
                    "layout" : {
                        "type" : "vertical",
                        "margin" : [6,6,6,6],
                        "spacing" : 0,

                        "widgets" : [
                            {
                                "type" : "tabwidget",
                                "stylesheet" : "QTabWidget::pane{border:none;}QTabWidget::tab-bar {alignment: center;}QTabBar::tab{background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 129, 255, 255), stop:1 rgba(82, 170, 255, 236));margin-right:10px;min-width:80px;min-height:20px;border:none;border-radius:2px;padding:2px;}QTabBar::tab:selected, QTabBar::tab:hover {background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #e7e7e7, stop: 0.4 #e7e7e7,stop: 0.5 #e7e7e7, stop: 1.0 rgba(211, 211, 211,150));color:black;border-bottom:1px solid red;}",
                                "tabs" : [
                                    {
                                        "title" : "Basic",
                                        "layout" : {
                                            "type" : "vertical",
                                            "widgets": [
                                                {
                                                    "type": "scrollarea",
                                                    "stylesheet" : "color:DodgerBlue;background:transparent;border:none;",
                                                    "widget" : {
                                                        "type" : "frame",
                                                        "layout" : {
                                                            "type" : "vertical",
                                                            "margin" : [0,0,0,0],
                                                            "spacing" : 10,
                                                            "widgets" : [
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Fetch Timer :"
                                                                            },
                                                                            {
                                                                                "id" : "fetchSpinBox",
                                                                                "type" : "spinbox",
                                                                                "range" : [3000,9000],
                                                                                "value" : 3000,
                                                                                "stylesheet" : "color:ghostwhite;border: 2px solid;border-color:DodgerBlue;border-radius:7px;"
                                                                            }
                                                                        ]
                                                                            
                                                                        
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Blur Effect :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                            
                                                                        
                                                                    }
                                                                    
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Blur Level :"
                                                                            },
                                                                            {
                                                                                "type" : "slider",
                                                                                "anchor" : "center",
                                                                                "orientation" : "Horizontal",
                                                                                "width" : 150,
                                                                                "stylesheet" : "QSlider {margin-top: 9px;margin-bottom: 9px;}QSlider::groove:horizontal{border: #000088;border-radius:4px;height: 8px;background: rgba(82, 170, 255, 236);margin: 2px 0;}QSlider::handle:horizontal {background-color: #1e90ff;border: 2px solid #1e90ff;width: 16px;height: 20px;line-height: 20px;margin-top: -5px;margin-bottom: -5px;border-radius: 9px; }QSlider::add-page:horizontal{background: rgb(200,200,200);height: 8px;margin: 2px 0;border-radius:4px;}"
            
                                                                            }
                                                                        ]
                                                                            
                                                                        
                                                                    }
                                                                    
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Game Activity :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "checked" : true,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                            
                                                                        
                                                                    }
                                                                    
                                                                },
                                                                {
                                                                    "id" : "joinButton",
                                                                    "type" : "button",
                                                                    "anchor" : "center",
                                                                    "text" : "RESET",
                                                                    "width" : 131,
                                                                    "height" : 32,
                                                                    "cursor" : "PointingHandCursor",
                                                                    "stylesheet" : "QPushButton{background:rgba(0, 0, 51, 130);font-family:'Century Gothic';font-weight:bold;color:white;border:2px solid;border-color:#4a455a;border-radius:10px;}",
                                                                    "animation" : {
                                                                        "type" : "color",
                                                                        "start_value" : ["#4a455a"],
                                                                        "end_value" : ["DodgerBlue"],
                                                                        "duration" : 800,
                                                                        "trigger" : "hover",
                                                                        "property" : "border"
                                                                    }
                                                                }
                                                            ]
                                                        }
                                                    }
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        "title" : "LAUNCHER",
                                        "layout" : {
                                            "type" : "vertical",
                                            "widgets" : [
                                                {
                                                    "type" : "scrollarea",
                                                    "stylesheet" : "color:DodgerBlue;background:transparent;border:none;",
                                                    "widget" : {
                                                        "type" : "frame",
                                                        "layout" : {
                                                            "type" : "vertical",
                                                            "margin" : [0,0,0,0],
                                                            "spacing" : 10,
                                                            "widgets" : [
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Border Color :"
                                                                            },
                                                                            {
                                                                                "id" : "bdColorButton",
                                                                                "type" : "button",
                                                                                "anchor" : "center",
                                                                                "width" : 150,
                                                                                "height" : 20,
                                                                                "stylesheet" : "background:white;border-radius:6px;"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Bar Color :"
                                                                            },
                                                                            {
                                                                                "id" : "barColorButton",
                                                                                "type" : "button",
                                                                                "anchor" : "center",
                                                                                "width" : 150,
                                                                                "height" : 20,
                                                                                "stylesheet" : "background:white;border-radius:6px;"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Border Transparency :"
                                                                            },
                                                                            {
                                                                                "type" : "slider",
                                                                                "anchor" : "center",
                                                                                "orientation" : "Horizontal",
                                                                                "width" : 150,
                                                                                "stylesheet" : "QSlider {margin-top: 9px;margin-bottom: 9px;}QSlider::groove:horizontal{border: #000088;border-radius:4px;height: 8px;background: rgba(82, 170, 255, 236);margin: 2px 0;}QSlider::handle:horizontal {background-color: #1e90ff;border: 2px solid #1e90ff;width: 16px;height: 20px;line-height: 20px;margin-top: -5px;margin-bottom: -5px;border-radius: 9px; }QSlider::add-page:horizontal{background: rgb(200,200,200);height: 8px;margin: 2px 0;border-radius:4px;}"
            
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Music Volume :"
                                                                            },
                                                                            {
                                                                                "type" : "slider",
                                                                                "anchor" : "center",
                                                                                "orientation" : "Horizontal",
                                                                                "width" : 150,
                                                                                "stylesheet" : "QSlider {margin-top: 9px;margin-bottom: 9px;}QSlider::groove:horizontal{border: #000088;border-radius:4px;height: 8px;background: rgba(82, 170, 255, 236);margin: 2px 0;}QSlider::handle:horizontal {background-color: #1e90ff;border: 2px solid #1e90ff;width: 16px;height: 20px;line-height: 20px;margin-top: -5px;margin-bottom: -5px;border-radius: 9px; }QSlider::add-page:horizontal{background: rgb(200,200,200);height: 8px;margin: 2px 0;border-radius:4px;}"
            
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Enable Music :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "checked" : true,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Visualize Song :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "checked" : true,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                    }
                                                                }
                                                                
                                                            ]
                                                        }

                                                    }
                                                    
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        "title" : "CHATBOX",
                                        "layout" : {
                                            "type" : "vertical",
                                            "widgets" : [
                                                {
                                                    "type" : "scrollarea",
                                                    "stylesheet" : "color:DodgerBlue;background:transparent;border:none;",
                                                    "widget" : {
                                                        "type" : "frame",
                                                        "layout" : {
                                                            "type" : "vertical",
                                                            "margin" : [0,0,0,0],
                                                            "spacing" : 10,
                                                            "widgets" : [
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Chat Notification :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "checked" : true,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Typing Status :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "checked" : true,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [0,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Text Font :"
                                                                            },
                                                                            {
                                                                                "id" : "fontSpinBox",
                                                                                "type" : "spinbox",
                                                                                "range" : [10,30],
                                                                                "value" : 15,
                                                                                "stylesheet" : "color:ghostwhite;border: 2px solid;border-color:DodgerBlue;border-radius:7px;"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "spacerItem",
                                                                    "hpolicy" : "fixed",
                                                                    "vpolicy" : "expanding"
                                                                }
                                                                
                                                            ]
                                                        }
                                                    }
                                                }
                                            ]
                                        }
                                    },
                                    {
                                        "title" : "EXPERIMENTAL",
                                        "layout" : {
                                            "type" : "vertical",
                                            "widgets" : [
                                                {
                                                    "type" : "scrollarea",
                                                    "stylesheet" : "color:DodgerBlue;background:transparent;border:none;",
                                                    "widget" : {
                                                        "type" : "frame",
                                                        "layout" : {
                                                            "type" : "vertical",
                                                            "margin" : [0,0,0,0],
                                                            "spacing" : 10,
                                                            "widgets" : [
                                                                {
                                                                    "type" : "label",
                                                                    "text" : "Graphics API"
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [20,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "DirectX 8 :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "checked" : true,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [20,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "DirectX 9 :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [20,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "DirectX 11 :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [20,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Vulkan :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [20,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Reshade DirectX 9 :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "type" : "frame",
                                                                    "layout" : {
                                                                        "type" : "horizontal",
                                                                        "margin" : [20,0,0,0],
                                                                        "spacing" : 0,
                                                                        "widgets" : [
                                                                            {
                                                                                "type" : "label",
                                                                                "text" : "Reshade DirectX 11 :"
                                                                            },
                                                                            {
                                                                                "type" : "switch",
                                                                                "anchor" : "center",
                                                                                "width" :  50,
                                                                                "height" : 20,
                                                                                "cursor" : "PointingHandCursor",
                                                                                "stylesheet" : "QSwitch::checked{background:DodgerBlue;}"
                                                                            }
                                                                        ]
                                                                    }
                                                                }

                                                            ]
                                                        }
                                                        
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                ]
                            },
                            {
                                "type" : "label",
                                "text" : "Do not turn off your computer while closing this window",
                                "alignment" : "Qt.AlignCenter",
                                "anchor" : "bottom",
                                "stylesheet" : "color:gray;"
                            }
                        ]
                    }
                }
            ]
        }
    }
    '''

    return json.loads(ui_data_json)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui_data = load_ui_data()
    parser = DynamicUIParser(ui_data,globals())
    window = parser.parse()
    window.show()
    sys.exit(app.exec_())

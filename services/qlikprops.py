from services.meta import FieldType, CLIENT_URL, new_uuid

def create_container_prop_table(tableid, mboxaddid, mboxeditid, mboxdelid):
    return {
        "qProp": {
            "qInfo": {
                "qType": "container"
            },
            "qMetaDef": {},
            "children": [
                {
                    "refId": tableid,
                    "label": "data_table",
                    "isMaster": False,
                    "condition": {
                      "qStringExpression": {
                        "qExpr": "=IF(vDataEntryMode = 0, 1, 0)"
                      }
                    }
                },
                {
                    "refId": mboxaddid,
                    "label": "data_add_mbox",
                    "isMaster": False,
                    "condition": {
                      "qStringExpression": {
                        "qExpr": "=IF(vDataEntryMode = 1, 1, 0)"
                      }
                    }
                },
                {
                    "refId": mboxeditid,
                    "label": "data_edit_mbox",
                    "isMaster": False,
                    "condition": {
                      "qStringExpression": {
                        "qExpr": "=IF(vDataEntryMode = 2, 1, 0)"
                      }
                    }
                },
                {
                    "refId": mboxdelid,
                    "label": "data_del_mbox",
                    "isMaster": False,
                    "condition": {
                      "qStringExpression": {
                        "qExpr": "=IF(vDataEntryMode = 3, 1, 0)"
                      }
                    }
                }
            ],
            "showTitles": False,
            "title": "",
            "subtitle": "",
            "footnote": "",
            "disableNavMenu": False,
            "showDetails": False,
            "showDetailsExpression": False,
            "borders": "auto",
            "showTabs": False,
            "useDropdown": True,
            "useScrollButton": True,
            "showIcons": False,
            "activeTab": "",
            "defaultTab": "",
            "visualization": "container",
            "qChildListDef": {
              "qData": {
                "visualization": "/visualization",
                "containerChildId": "/containerChildId",
                "qExtendsId": "/qExtendsId",
                "title": "/title",
                "showCondition": "/showCondition"
              }
            },
            "supportRefresh": False,
            "hasExternalChildren": False
        }
    }

def create_container_prop_btn1(btn1id, label1):
    return {
        "qProp": {
            "qInfo": {
                "qType": "container"
            },
            "qMetaDef": {},
            "children": [
                {
                    "refId": btn1id,
                    "label": label1,
                    "isMaster": False,
                    "condition": {
                        "qStringExpression": {
                            "qExpr": "=IF(vDataEntryMode > 0, 0, 1)"
                        }
                    }
                }
            ],
            "showTitles": False,
            "title": "",
            "subtitle": "",
            "footnote": "",
            "disableNavMenu": False,
            "showDetails": False,
            "showDetailsExpression": False,
            "borders": "auto",
            "showTabs": False,
            "useDropdown": True,
            "useScrollButton": True,
            "showIcons": False,
            "activeTab": "",
            "defaultTab": "",
            "visualization": "container",
            "qChildListDef": {
              "qData": {
                "visualization": "/visualization",
                "containerChildId": "/containerChildId",
                "qExtendsId": "/qExtendsId",
                "title": "/title",
                "showCondition": "/showCondition"
              }
            },
            "supportRefresh": False,
            "hasExternalChildren": False
        }
    }

def create_container_prop_btn2(btn1id, btn2id, label1, label2):
    return {
        "qProp": {
            "qInfo": {
                "qType": "container"
            },
            "qMetaDef": {},
            "children": [
                {
                    "refId": btn1id,
                    "label": label1,
                    "isMaster": False,
                    "condition": {
                        "qStringExpression": {
                            "qExpr": "=IF(vDataEntryMode > 0, 0, 1)"
                        }
                    }
                },
                {
                    "refId": btn2id,
                    "label": label2,
                    "isMaster": False,
                    "condition": {
                        "qStringExpression": {
                            "qExpr": "=IF(vDataEntryMode > 0, 1, 0)"
                        }
                    }
                }
            ],
            "showTitles": False,
            "title": "",
            "subtitle": "",
            "footnote": "",
            "disableNavMenu": False,
            "showDetails": False,
            "showDetailsExpression": False,
            "borders": "auto",
            "showTabs": False,
            "useDropdown": True,
            "useScrollButton": True,
            "showIcons": False,
            "activeTab": "",
            "defaultTab": "",
            "visualization": "container",
            "qChildListDef": {
              "qData": {
                "visualization": "/visualization",
                "containerChildId": "/containerChildId",
                "qExtendsId": "/qExtendsId",
                "title": "/title",
                "showCondition": "/showCondition"
              }
            },
            "supportRefresh": False,
            "hasExternalChildren": False
        }
    }

def create_sheet_prop_empty():
    return {
        "qProp": {
            "qInfo": {
                "qType": "sheet"
            }
        }
    }

def create_sheet_prop(sheettitle, tablecntrid, btn1cntrid, btn2cntrid, btn3cntrid):
    return {
        "qProp": {
            "qInfo": {
                "qType": "sheet"
            },
            "qMetaDef": {
                "title": sheettitle,
                "description": ""
            },
            "columns": 24,
            "rows": 12,
            'gridResolution': 'small',
            "rank": -1,
            "thumbnail": {
              "qStaticContentUrlDef": {}
            },            
            "qChildListDef": {
                "qData": {
                    "title": "/title"
                }
            },
            'gridMode': 'edit', 
            'gridResolution': 'small',
            'customRowBase': 24,
            "cells": [
                {
                    "name": tablecntrid,
                    "type": "container",
                    "col": 0,
                    "row": 1,
                    "colspan": 24,
                    "rowspan": 11,
                    "bounds": {
                        "y": 8.3333333333333321,
                        "x": 0,
                        "width": 100,
                        "height": 91.666666666666657
                    }
                },
                {
                    "name": btn1cntrid,
                    "type": "container",
                    "col": 0,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 1,
                    "bounds": {
                        "y": 0,
                        "x": 0,
                        "width": 16.666666666666664,
                        "height": 8.3333333333333321
                    }
                },
                {
                    "name": btn2cntrid,
                    "type": "container",
                    "col": 4,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 1,
                    "bounds": {
                        "y": 0,
                        "x": 16.666666666666664,
                        "width": 16.666666666666664,
                        "height": 8.3333333333333321
                    }
                },
                {
                    "name": btn3cntrid,
                    "type": "container",
                    "col": 8,
                    "row": 0,
                    "colspan": 4,
                    "rowspan": 1,
                    "bounds": {
                        "y": 0,
                        "x": 33.333333333333329,
                        "width": 16.666666666666664,
                        "height": 8.3333333333333321
                    }
                }
            ]
        }
    }

def create_mediabox_prop(sheettitle, mboxid, mode):
    return {
        "qProp": {
            "qInfo": {
                "qType": "swr-mediabox"
            },
            "qMetaDef": {},
            "showTitles": False,
            "title": "",
            "subtitle": "",
            "footnote": "",
            "disableNavMenu": False,
            "showDetails": False,
            "showDetailsExpression": False,
            "props": {
              "mbType": "website",
              "image": {
                "source": "",
                "horizontalAlign": "left",
                "verticalAlign": "top",
                "imageAspectRatio": "bestfit"
              },
              "html": {
                "source": "<div style=\"font-weight:bold;color: darkgreen;\">This is the MediaBox</div>",
                "scrollBehavior": "auto"
              },
              "website": {
                "source": {
                  "qStringExpression": {
                    "qExpr": f"='{CLIENT_URL}?mode={mode}&appid=' & DocumentName() & '&dbtable={sheettitle}'"
                  }
                },
                "scrollBehavior": "none",
                "interaction": True
              },
              "video": {
                "videoType": "video-mp4",
                "poster": "",
                "sourceMP4": "",
                "sourceYouTube": ""
              }
            },
            "visualization": "swr-mediabox",
            "version": "0.4.5",
            "extensionMeta": {
              "translationKey": "",
              "icon": "puzzle",
              "iconChar": "puzzle",
              "isLibraryItem": True,
              "visible": True,
              "name": "Media Box",
              "description": "Include web pages, videos, images and much more into your Qlik Sense app.<br/><br/>(Version: 0.4.5)",
              "template": "swr-mediabox",
              "iconPath": "M14.5,9 L13,9 L13,3.3 C13,3.1 12.9,3 12.7,3 L8,3 L8,1.5 C8,0.7 7.3,0 6.5,0 C5.7,0 5,0.7 5,1.5 L5,3 L0.3,3 C0.1,3 0,3.1 0,3.3 L0,9 L1.5,9 C2.3,9 3,9.7 3,10.5 C3,11.3 2.3,12 1.5,12 L0,12 L0,15.7 C0,15.9 0.1,16 0.3,16 L5,16 L5,14.5 C5,13.7 5.7,13 6.5,13 C7.3,13 8,13.7 8,14.5 L8,16 L12.7,16 C12.9,16 13,15.9 13,15.7 L13,12 L14.5,12 C15.3,12 16,11.3 16,10.5 C16,9.7 15.3,9 14.5,9 Z",
              "isThirdParty": True,
              "type": "visualization",
              "version": "0.4.5",
              "preview": "mediabox.png",
              "author": "Stefan Walther",
              "previewIconURL": "https://kokpit.tcmb.gov.tr/extensions/swr-mediabox/mediabox.png"
            },
            "qLayoutExclude": {"disabled": {}},
            "containerChildId": mboxid
        }
    }

def create_table_prop(tableid, fields, qid=None):
    return {
        "qProp": {
            "qInfo": {
                "qId": qid,
                "qType": "table"
            },
            "qMetaDef": {},
            "qHyperCubeDef": {
                "qDimensions": [create_dimension_prop(*field) for field in fields],
                "qMeasures": [],
                "qInterColumnSortOrder": [i for i in range(len(fields))],
                "qSuppressMissing": True,
                "qInitialDataFetch": [
                    {
                        "qLeft": 0,
                        "qTop": 0,
                        "qWidth": 0,
                        "qHeight": 0
                    }
                ],
                "qReductionMode": "N",
                "qMode": "S",
                "qPseudoDimPos": -1,
                "qNoOfLeftDims": -1,
                "qMaxStackedCells": 5000,
                "qCalcCond": {},
                "qTitle": {},
                "qCalcCondition": {"qCond": {}, "qMsg": {}},
                "qColumnOrder": [i for i in range(len(fields))],
                "qExpansionState": [],
                "qDynamicScript": [],
                "columnOrder": [i for i in range(len(fields))],
                "columnWidths": [-1 for _ in range(len(fields))],
                "qLayoutExclude": {
                    "qHyperCubeDef": {
                        "qDimensions": [],
                        "qMeasures": [],
                        "qInterColumnSortOrder": [],
                        "qInitialDataFetch": [],
                        "qReductionMode": "N",
                        "qMode": "S",
                        "qPseudoDimPos": -1,
                        "qNoOfLeftDims": -1,
                        "qMaxStackedCells": 5000,
                        "qCalcCond": {},
                        "qTitle": {},
                        "qCalcCondition": {"qCond": {}, "qMsg": {}},
                        "qColumnOrder": [],
                        "qExpansionState": [],
                        "qDynamicScript": []
                    }
                }
            },
            "script": "",
            "search": {"sorting": "auto"},
            "showTitles": False,
            "title": "",
            "subtitle": "",
            "footnote": "",
            "disableNavMenu": False,
            "showDetails": False,
            "showDetailsExpression": False,
            "totals": {"show": False, "position": "noTotals", "label": "Totals"},
            "scrolling": {"horizontal": True, "keepFirstColumnInView": False, "keepFirstColumnInViewTouch": False},
            "multiline": {"wrapTextInHeaders": True, "wrapTextInCells": True},
            "visualization": "table",
            "qLayoutExclude": {"disabled": {}, "quarantine": {}},
            "containerChildId": tableid
        }
    }

def create_dimension_prop(fieldname, fieldheader, fieldtype, fieldenum):
    new_line = '\n'
    d_apost = "''"
    return {
        "qDef": {
            "qGrouping": "N",
            "qFieldDefs": [f"=IF({fieldname} = 1, 'Evet', IF({fieldname} = 0, 'Hayır', {fieldname}))" if fieldtype == FieldType.BOOLEAN.value else 
                        f"={new_line.join([f'IF({fieldname}={fe[1]}, {fe[0]},' for fe in fieldenum + [['Null()', d_apost]]])} Null(){''.join([')' for _ in range(len(fieldenum) + 1)])}" 
                        if fieldtype == FieldType.MENU.value else fieldname],
            "qFieldLabels": [fieldheader],
            "qSortCriterias": [
                {
                    "qSortByNumeric": 1,
                    "qSortByAscii": 1,
                    "qSortByLoadOrder": 1,
                    "qExpression": {}
                }
            ],
            "qNumberPresentations": [],
            "qActiveField": 0,
            "autoSort": True,
            "cId": new_uuid(),
            "othersLabel": "Others",
            "textAlign": {"auto": True, "align": "left"},
            "representation": {
                "type": "text",
                "urlPosition": "dimension",
                "urlLabel": "",
                "linkUrl": "",
                "imageSetting": "label",
                "imageLabel": "",
                "imageUrl": "",
                "imageSize": "fitHeight",
                "imagePosition": "topCenter"
            }
        },
        "qOtherTotalSpec": {
            "qOtherMode": "OTHER_OFF",
            "qOtherCounted": {"qv": "10"},
            "qOtherLimit": {"qv": "0"},
            "qOtherLimitMode": "OTHER_GE_LIMIT",
            "qForceBadValueKeeping": True,
            "qApplyEvenWhenPossiblyWrongResult": True,
            "qOtherSortMode": "OTHER_SORT_DESCENDING",
            "qTotalMode": "TOTAL_OFF",
            "qReferencedExpression": {}
        },
        "qOtherLabel": {"qv": "Others"},
        "qTotalLabel": {},
        "qCalcCond": {},
        "qAttributeExpressions": [],
        "qAttributeDimensions": [],
        "qCalcCondition": {"qCond": {}, "qMsg": {}}
    }

def create_button_prop(btnid, value, label):
    return {
        "qProp": {
            "qInfo": {
                # "qId": "6e0b5a80-c556-4f72-afc8-8c734e636a0e",
                "qType": "action-button"
            },
            "qMetaDef": {},
            "actions": [
                {
                    "actionLabel": "",
                    "actionType": "setVariable",
                    "bookmark": "",
                    "field": "",
                    "variable": "vDataEntryMode",
                    "showSystemVariables": False,
                    "softLock": False,
                    "value": value,
                    "partial": False,
                    "automation": "",
                    "automationPostData": False,
                    "cId": new_uuid()
                }
            ],
            "navigation": {
                "action": "none",
                "appId": "",
                "sheet": "",
                "story": "",
                "websiteUrl": "",
                "sameWindow": False,
                "odagLink": ""
            },
            "useEnabledCondition": False,
            "enabledCondition": 1,
            "showTitles": False,
            "title": "",
            "subtitle": "",
            "footnote": "",
            "disableNavMenu": False,
            "showDetails": False,
            "showDetailsExpression": False,
            "style": {
                "label": label,
                "font": {
                    "size": 0.5,
                    "useColorExpression": False,
                    "color": {"index": -1, "color": None},
                    "colorExpression": "",
                    "style": {"bold": True, "italic": False, "underline": False},
                    "align": "center"
                },
                "background": {
                    "useColorExpression": False,
                    "color": {"index": -1, "color": None},
                    "colorExpression": "",
                    "useImage": False,
                    "size": "auto",
                    "position": "centerCenter",
                    "url": {"qStaticContentUrlDef": {}}
                },
                "border": {
                    "useBorder": False,
                    "radius": 0,
                    "width": 0,
                    "useColorExpression": False,
                    "color": {"index": -1, "color": None},
                    "colorExpression": ""
                },
                "icon": {
                    "useIcon": False,
                    "iconType": "",
                    "position": "left"
                }
            },
            "visualization": "action-button",
            "version": "1.27.0",
            "containerChildId": btnid
        }
    }
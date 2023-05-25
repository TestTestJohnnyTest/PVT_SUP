x = """1009,pastebin.com
1012,aa.com
1020,avast.com
1030,cdninstagram.com
1032,creditkarma.com
1033,gmanetwork.com
1041,rightmove.co.uk
1042,tmz.com
1045,abcnews.go.com
1046,icy-veins.com
1047,mixplugin.com
1054,dawn.com
1056,nextdoor.com
1057,harvard.edu
1063,biblegateway.com
1064,nasa.gov
1066,filmfanatic.com
1070,knowyourmeme.com
1072,chess.com
1076,farsnews.com
1078,smallpdf.com
1079,pcmag.com
1084,ted.com
1087,gumtree.com
1100,gap.com
1101,royalbank.com
1106,istockphoto.com
1124,ebay.ca
1139,quizzstar.com
1143,skyscanner.net
1147,cookpad.com
1150,opensubtitles.org
1165,shopclues.com
1166,utorrent.com
1167,nanoadexchange.com
1169,basecamp.com
1194,people.com
1196,weather.gov
1209,gamestop.com
1231,teamviewer.com
1232,readthedocs.io
1233,besoccer.com
1234,marketwatch.com
1250,worldofwarcraft.com
1255,kongregate.com
1259,plex.tv
1260,fandango.com
1265,wargaming.net
1267,getbootstrap.com
1287,cloudflare.com
1297,televisionfanatic.com
1298,online-convert.com
1321,movieweb.com
1328,rockstargames.com
1333,gofundme.com
1334,mathworks.com
1340,apartmenttherapy.com
1367,healthline.com
1371,mcafee.com
1374,hollywoodreporter.com
1376,freelancer.com
1377,thevintagenews.com
1379,verizon.com
1387,stumbleupon.com
1388,bettersearchtools.com
1400,digitalocean.com
1401,leadzupc.com
1405,irs.gov
1415,gameforge.com
1418,urbanoutfitters.com
1424,oneplus.net
1430,nationalgeographic.com
1433,theweathernetwork.com
1441,iflscience.com
1455,emailaccessonline.com
1468,forgeofempires.com
1474,garmin.com
1475,foodnetwork.com
1478,nintendo.com
1488,minecraft.net
1541,programme-tv.net
1543,githubusercontent.com
1548,thingiverse.com
1559,invisionapp.com
1567,jetbrains.com
1569,epochtimes.com
1570,digitaltrends.com
1572,entrepreneur.com
1573,gog.com
1575,pcpartpicker.com
1595,trustpilot.com
1599,walgreens.com
1603,miniclip.com
1604,coursehero.com
1608,oceanofgames.com
1609,lostfilm.tv
1610,newstrend.news
1612,myworkday.com
1614,jquery.com
1619,vmware.com
1633,chegg.com
1634,malwarebytes.com
1640,informer.com
1644,swagbucks.com
1647,adidas.com
1655,ubuntu.com
1661,sonyentertainmentnetwork.com
1664,square-enix.com
1670,nexusmods.com
1685,mydrivers.com
1686,autotrader.com"""

my_list = x.split("\n")
print(my_list)
my_dict = {}
counter = 207
for each in my_list:
    each = each[5:]
    my_dict[counter] = each
    counter += 1
    print(each)

my_list = list(my_dict.values())

import json
print(json.dumps(my_dict))


WEBSITE_LIST = {
                "https://www.youtube.com/":{
                    "specifics":"ablock=true;",
                        "main_menu":'refresh_sens:id;guide-icon',
                        "endpoints":
                        { 
                        "login-page":   'direct-link;signin',
                        "video":  'css selector;ytd-rich-item-renderer'
                        },
                        "sub-endpoints":
                        {
                            "main_menu":{"trending":'relies_prev:partial link text;Trending',
                                        "music":   'relies_prev:partial link text;Music',
                                        "gaming":  'relies_prev:partial link text;Gaming',
                                        "news":    'relies_prev:partial link text;News',
                                        "sports":  'relies_prev:partial link text;Sports',
                                        "learning":'relies_prev:partial link text;Learning'
                                        },
                            "trending":{"video":'rand_ind:css selector;ytd-video-renderer'
                                        },
                            "music":{"video":'rand_ind:css selector;ytd-video-renderer'
                                    },
                            "gaming":{"video":"rand_ind:css selector;ytd-video-renderer"
                            },
                        }
                    },





                "https://www.pastebin.com":{
                    "specifics":"ablock=true;",
                    "endpoints":{
                        "API": "direct-link;doc_api",
                        "tools": "direct-link;tools",
                        "faq": "direct-link;faq",
                        "Login": "login",
                        "sign-up": "signup"
                    },
                    "sub-endpoints":{
                        "header":{
                            "API": "direct-link;doc_api",
                            "tools": "direct-link;tools",
                            "faq": "direct-link;faq",
                            "Login": "direct-link;login",
                            "sign-up": "direct-link;faq"
                        },
                        "API":{"direct-link;doc_api", 
                            "direct-link;doc_scraping_api", 
                            "direct-link;languages"
                            },
                        "tools": {"direct-link;tools", 
                                "direct-link;dSyh0xCc"\
                        },
                        "faq": {"direct-link;faq", 
                                "direct-link;doc_terms_of_service"
                        }
                    }
                },
                "https://www.aa.com":{
                    "specifics":"ablock=true;",
                    "main_page":"refresh_sens:name;optoutmulti_button",
                    "endpoints":{
                    "log_in":"id;log-in-button",
                    "join":"id;join-button",
                    "plan_travel":"refresh_sens:id;plan-travel-expander",
                    "travel_info":"refresh_sens:id;travel-information-expander",
                    "aadvantage":"refresh_sens:id;aadvantage-expander"
                    },
                    "sub-endpoints":
                    {
                        "plan_travel": {"refresh_sens:id;plan-travel-expander", 
                                        "relies_prev:partial link text;Flights", 
                                        "partial link text; Travelling with infants ", 
                                        "partial link text;Call Special Assistance"},
                        "travel_info": {"refresh_sens:id;travel-information-expander", 
                                        "relies_prev:partial link text;At the airport", 
                                        "partial link text;Check flight status"},
                        "aadvantage": {
                                    "refresh_sens:id;aadvantage-expander",
                                    "relies_prev:partial link text;AAdvantage", 
                                    "direct-link;pubcontent/en_US/aadvantage-program/loyalty-points/index.html"}
                    }
                },
                "https://www.avast.com":{
                    "specifics":"ablock=true;",
                    "endpoints":{
                    "for_home":"partial link text;For home",
                    "for_business":"partial link text;For business",
                    "for_partners":"partial link text;For partners",
                    "about_us":"partial link text;About us"
                    },
                    "sub-endpoints":
                    {
                        "for_business":{"partial link text;For business", 
                                        "rand_int:class name;btn-wrapper", 
                                        "rand_int:class name;header-more"},
                        "for_partners":{"relies_prev:partial link text;For partners", 
                                        "direct-link;en-ca/partners/smartlife",
                                        "class name;btn-primary"}
                    }
                },
                "https://www.instagram.com/":{
                    "specifics":"ablock=true;",
                    "endpoints":{

                    }
                }
            }

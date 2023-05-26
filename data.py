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
                        "Login":"direct-link;login",
                        "sign-up":"direct-link;signup",
                        "languages":"direct-link;languages",
                        "manual":"direct-link;dSyh0xCc",
                        "site_tos":"direct-link;faq, direct-link;doc_terms_of_service"
                    },
                    "sub-endpoints":{
                        "header":{
                            "API": "direct-link;doc_api",
                            "tools": "direct-link;tools",
                            "faq": "direct-link;faq",
                            "Login": "direct-link;login",
                            "sign-up": "direct-link;faq"
                        },
                        "API":{
                            "scraping_api":"direct-link;doc_scraping_api"
                        },
                        "scraping_api":{
                            ## end ##
                            "languages":"direct-link;languages"
                        },
                        "tools": {
                            ## end ##
                            "manual":"direct-link;dSyh0xCc"
                        },
                        "faq": {
                            ## end ##
                            "site_tos":"direct-link;doc_terms_of_service"
                        }
                    }
                },
                "https://www.aa.com":{
                    "specifics":"ablock=true;",
                    "main_page":"refresh_sens:name;optoutmulti_button",
                    "endpoints":{
                        "log_in":"id;log-in-button",
                        "join":"id;join-button",
                        "special_assist":
                            "relies_prev:partial link text;Flights, partial link text; Travelling with infants , partial link text;Call Special Assistance",
                        "flight_status":
                            "relies_prev:partial link text;At the airport, partial link text;Check flight status",
                        "loyalty_points":
                            "relies_prev:partial link text;AAdvantage, direct-link;pubcontent/en_US/aadvantage-program/loyalty-points/index.html"
                        },
                    "sub-endpoints":{
                        "plan_travel": {
                            "flights":"refresh_sens:id;plan-travel-expander"
                        },
                        "flights":{
                            "infants":"partial link text; Travelling with infants "
                        },
                        "infants":{
                            ## end ##
                            "special_assist":"partial link text;Call Special Assistance"
                        },

                        "travel_info":{
                            "info_menu":"refresh_sens:id;travel-information-expander"
                        },
                        "info_menu":{
                            ## end ##
                            "flight_status":"partial link text;Check flight status"
                        },
                        "aadvantage":{
                            "aadvantage_menu":"refresh_sens:id;aadvantage-expander"
                        },
                        "aadvantage_menu":{
                            "aadvantage_menu2":"relies_prev:partial link text;AAdvantage"
                        },
                        "aadvantage_menu2":{
                            ## end ##
                            "loyalty_points":"relies_prev:partial link text;AAdvantage"
                        }
                    }
                },

#########EVERYTHING BELOW HERE IS NOT CORRECTLY FORMATTED
                "https://www.avast.com":{
                    "specifics":"ablock=true;",
                    "endpoints":{
                        "for_home":"partial link text;For home",
                        "about_us":"partial link text;About us",
                        "store_closeup":"class name;btn-wrapper, rand_ind:class name;header-more",
                        "faq":"direct-link;en-ca/partners/smartlife, class name;btn-primary"
                    },
                    "sub-endpoints":{
                        "for_business":{
                                "store":"partial link text;For business"
                        },
                        "store":{
                            ## end ##
                            "store_closeup":"class name;btn-wrapper"
                        },
                        "for_partners":{
                            "smartlife":"relies_prev:partial link text;For partners"
                        },
                        "smartlife":{
                            ## end ##
                           "faq":"direct-link;en-ca/partners/smartlife"     
                        }
                    }
                },
                "https://www.instagram.com/":{
                    "specifics":"ablock=true;",
                    "endpoints":{
                        "sign_up":"partial link text;Sign up",
                        "footer":"tag name;footer"
                    },
                    "sub-endpoints":{
                        "footer":{
                            "tag name;footer", 
                            "relies_prev:class name;x9f619",
                            "rand_ind:tag name;a"}
                    }
                },
                "https://www.creditkarma.com/":{
                    "specifics":"ablock=true;",
                    "endpoints":{
                        "button_list":"class name;flat-card-root",
                        "login":"direct-link;auth/logon"
                    },
                    "sub-endpoints":{
                        #2/6 of buttons need login auth
                        "cards": "rand_ind:partial link text;Continue",
                        "autos": "rand_ind:partial link text;Get Started",
                    }
                },
                #Really bad response time
                "https://www.gmanetwork.com":{
                    "specifics":"ablock=true;",
                    "endpoints":{
                        "button_list":"id;feature-widget",
                        "news":"partial link text;News",

                    },
                    "sub-endpoints":{
                        "button_list":"rand_ind:class name;feature-main"
                    }
                },
                "https://www.rightmove.co.uk":{
                    "specifics":"ablock=true;",
                    "endpoints":{
                        "article_list":"rand_ind:xpath;//article[@class='DesktopPod_desktopPod__22rpL']/a",
                        "sign_in":"partial link text;Sign in"
                    },
                    "sub-endpoints":{
                        
                        "sold_house_prices":
                            "rand_ind:xpath;//div[@class='linksCollection_linkCellOne__xYsbL']/a",
                        "property_news":
                            "scroll_2500~rand_ind:class name;article-block__link",
                        "moving_stories":""
                    }
                }

            }
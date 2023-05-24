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
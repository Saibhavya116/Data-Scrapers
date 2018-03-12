#!/usr/local/bin/python3.6

import facebook

graph = facebook.GraphAPI(access_token='EAACEdEose0cBACok2rDjPPZCm7sG3qJvCcdJkxYKu7ZBkEnKOGBsF63RF7nTUWZBQA5x0d1N5nxDCFbzDdpxI40hzT7ddlv2CHIIYVv1HypSEBCxTZBhNqZBjeRFWd77Rsf8VbSqnox6AJKuTmPjvFT3jZCqV3JrSSzzLPY3KdYRNlbv8zoM8PJSbcmXRCWDsZD',version='2.10')
events=graph.request('me?fields=id,name,friends.limit(100){name,likes.limit(150){place_topics{name},category,fan_count,global_brand_page_name}}') 


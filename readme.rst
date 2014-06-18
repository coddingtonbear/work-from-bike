
Map Extents
-----------

WGS84: -124.1757,45.2614,-122.4728,46.2388


Finding WIFI APs
----------------

AT&T WiFI
~~~~~~~~~

* URL: https://www.att.com/apis/maps/v2/locator/search/viewport.json
* Method: GET
* Sample Data::

  // As GET params
  {
      "apikey": "27d684f8e73c701f4e41b334813b54cf3c7fa46d",
      "channels": "wifibasic",
      "ne": "46.623148673084934,-123.3080316015625",
      "origin": "46.18977,-123.83395",
      "poi_types": "wifi",
      "select": "id,name,notes,services,phone,channel,address1,address2,addr_hint,city,postal,region,lon,lat,hours,ssid",
      "sw": "45.710113170957875,-124.5802483984375"
  }

* Sample Response::

  {
      "allcount": 7,
      "auth_results": "valid",
      "copyright": "\u00a92012 AT&T Intellectual Property. All rights reserved. AT&T, the AT&T logo and all other AT&T marks contained herein are trademarks of AT&T Intellectual Property and/or AT&T affiliated companies.",
      "count": 7,
      "deprecation_date": "",
      "endoflife_date": "",
      "errors": null,
      "lang": "en",
      "logourl": "http://www.att.com/Common/indc/images/logo.gif",
      "moddt": {
          "country": "2014-05-06T07:15:25+0000",
          "pos": "2014-06-17T20:20:00+0000",
          "ship": "2014-05-06T07:15:25+0000",
          "wifi": "2014-06-13T07:09:30+0000"
      },
      "origin": {
          "lat": "46.18977",
          "lon": "-123.83395"
      },
      "query": {
          "apikey": [
              "27d684f8e73c701f4e41b334813b54cf3c7fa46d"
          ],
          "channels": [
              "wifibasic"
          ],
          "ne": [
              "46.623148673084934,-123.3080316015625"
          ],
          "origin": [
              "46.18977,-123.83395"
          ],
          "poi_types": [
              "wifi"
          ],
          "select": [
              "id,name,notes,services,phone,channel,address1,address2,addr_hint,city,postal,region,lon,lat,hours,ssid"
          ],
          "sw": [
              "45.710113170957875,-124.5802483984375"
          ]
      },
      "resp_code": 0,
      "results": [
          {
              "address1": "645 Marine Dr",
              "channel": 1000,
              "city": "Astoria",
              "id": "RASB-U00169XM",
              "lat": 46.19039,
              "lon": -123.83607,
              "name": "McDonald's",
              "postal": "97103-4238",
              "region": "OR",
              "services": [
                  1002
              ],
              "ssid": "attwifi"
          },
          {
              "address1": "350 Marine Dr",
              "channel": 1000,
              "city": "Astoria",
              "id": "RASB-U0017RT4",
              "lat": 46.190533,
              "lon": -123.8391,
              "name": "Burger King #6047",
              "postal": "97103-4328",
              "region": "OR",
              "services": [
                  1002
              ],
              "ssid": "attwifi"
          },
          {
              "address1": "159 S Highway 101",
              "channel": 1000,
              "city": "Warrenton",
              "id": "RASB-U0017R1A",
              "lat": 46.161125,
              "lon": -123.89915,
              "name": "ATT Retail Store DBID#  86375",
              "postal": "97146-9314",
              "region": "OR",
              "services": [
                  1002
              ],
              "ssid": "attwifi"
          },
          {
              "address1": "1650 SE Ensign Ln",
              "channel": 1000,
              "city": "Warrenton",
              "id": "RASB-U0017V4J",
              "lat": 46.14838,
              "lon": -123.91815,
              "name": "The Home Depot #4023",
              "postal": "97146-7338",
              "region": "OR",
              "services": [
                  1002
              ],
              "ssid": "attwifi"
          },
          {
              "address1": "177  USHWY 101",
              "channel": 1000,
              "city": "Warrenton",
              "id": "RASB-U001671C",
              "lat": 46.139362,
              "lon": -123.91772,
              "name": "STARBUCKS 10467",
              "postal": "97146",
              "region": "OR",
              "services": [
                  1002
              ],
              "ssid": "attwifi"
          },
          {
              "address1": "225 S Roosevelt Dr",
              "channel": 1000,
              "city": "Seaside",
              "id": "RASB-U00169VT",
              "lat": 45.99224,
              "lon": -123.92105,
              "name": "McDonald's",
              "postal": "97138-6741",
              "region": "OR",
              "services": [
                  1002
              ],
              "ssid": "attwifi"
          },
          {
              "address1": "100 16th St SE",
              "channel": 1000,
              "city": "Long Beach",
              "id": "RASB-U00169J5",
              "lat": 46.341946,
              "lon": -124.05433,
              "name": "McDonald's",
              "postal": "98631-3694",
              "region": "WA",
              "services": [
                  1002
              ],
              "ssid": "attwifi"
          }
      ],
      "status": 200,
      "termsurl": "http://www.att.com/gen/general?pid=11561",
      "viewport": {
          "ne": {
              "lat": 46.341946,
              "lon": -123.70156
          },
          "sw": {
              "lat": 45.99224,
              "lon": -124.188835
          }
      }
  }

WeFi
~~~~


* URL: http://www.wefi.com/maps/data.ajax.php
* Method: POST
* Sample Data::

  // In form variable named 'data'; JSON-encoded
  {
      "action": 1,
      "lat": 46.18011142223147,
      "lng": -123.8492720901184,
      "radius": 4361,
      "zoom": 14
  }

* Sample Response::

  {
      "aps": [
          {
              "CNRID": "11871497",
              "SSID": "ClatsopCommunity",
              "apGroup": "1",
              "apName": "Clatsop Community College",
              "category": "18",
              "displayGroup": "10",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "11871497",
                  "City": "Astoria",
                  "Country": "US",
                  "State": "OR",
                  "Street": "1653 Jerome Avenue",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "2",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.183745",
              "loginType": "eUnknown",
              "long": "-123.82447"
          },
          {
              "CNRID": "25045458",
              "SSID": "COA Library",
              "apGroup": "5",
              "apName": "City of Astoria  Library",
              "category": "5",
              "displayGroup": "10",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "25045458",
                  "City": "Astoria",
                  "Country": "US",
                  "State": "OR",
                  "Street": "450 10th St",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "0",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.18802",
              "loginType": "eUnknown",
              "long": "-123.83246"
          },
          {
              "CNRID": "134115870",
              "SSID": "ClatsopCounty",
              "apGroup": "1",
              "apName": [],
              "category": "14",
              "displayGroup": "20",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "134115870",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "0",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.189133012499994",
              "loginType": "eUnknown",
              "long": "-123.83362666250001"
          },
          {
              "CNRID": "81508825",
              "SSID": "RileaMWR7025",
              "apGroup": "1",
              "apName": "Red Lion Inn Astoria",
              "category": "7",
              "displayGroup": "20",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "81508825",
                  "City": "Astoria",
                  "Country": "US",
                  "State": "OR",
                  "Street": "400 Industry St",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "2",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.186346",
              "loginType": "eUnknown",
              "long": "-123.857898"
          },
          {
              "CNRID": "1065079",
              "SSID": "Astoria Library",
              "apGroup": "1",
              "apName": "Astoria Public Library",
              "category": "5",
              "displayGroup": "10",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "1065079",
                  "City": " Astoria",
                  "Country": "US",
                  "State": "OR",
                  "Street": "450 10th St",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "0",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.1880219",
              "loginType": "eUnknown",
              "long": "-123.832455"
          },
          {
              "CNRID": "16378464",
              "SSID": "RedLion",
              "apGroup": "1",
              "apName": "Red Lion Inn Astoria",
              "category": "7",
              "displayGroup": "10",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "16378464",
                  "City": "Astoria",
                  "Country": "US",
                  "State": "OR",
                  "Street": "400 Industry St",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "2",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.188668",
              "loginType": "eUnknown",
              "long": "-123.855962"
          },
          {
              "CNRID": "17894281",
              "SSID": "MT_HOME",
              "apGroup": "1",
              "apName": "Holiday Inn Express Astoria",
              "category": "7",
              "displayGroup": "10",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "17894281",
                  "City": "Astoria",
                  "Country": "US",
                  "State": "OR",
                  "Street": "204 w marine dr",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "2",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.1899031",
              "loginType": "eUnknown",
              "long": "-123.8478543"
          },
          {
              "CNRID": "43036624",
              "SSID": "ClatsopCounty",
              "apGroup": "1",
              "apName": "Clatsop County Courthouse",
              "category": "33",
              "displayGroup": "20",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "43036624",
                  "City": "Astoria",
                  "Country": "United States",
                  "State": "OR",
                  "Street": "749 Commercial St",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "0",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.189031766002",
              "loginType": "eUnknown",
              "long": "-123.83525639249"
          },
          {
              "CNRID": "11870203",
              "SSID": "ClatsopCommunity",
              "apGroup": "1",
              "apName": "Clatsop Community College",
              "category": "18",
              "displayGroup": "10",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "11870203",
                  "City": " Astoria",
                  "Country": "US",
                  "State": "OR",
                  "Street": "1653 Jerome Ave",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "0",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.183744",
              "loginType": "eUnknown",
              "long": "-123.824423"
          },
          {
              "CNRID": "71644446",
              "SSID": "wetdog-cafe",
              "apGroup": "1",
              "apName": "Wet Dog Cafe",
              "category": "8",
              "displayGroup": "10",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "71644446",
                  "City": " Astoria",
                  "Country": "US",
                  "State": "OR",
                  "Street": "144 11th St",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "0",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.190165",
              "loginType": "eUnknown",
              "long": "-123.831405"
          },
          {
              "CNRID": "17950814",
              "SSID": "Astoria Coffee House",
              "apGroup": "1",
              "apName": "Astoria Coffee House",
              "category": "8",
              "displayGroup": "10",
              "distance": "0.0",
              "geoInfo": {
                  "CNRID": "17950814",
                  "City": " Astoria",
                  "Country": "US",
                  "State": "OR",
                  "Street": "243 11th St",
                  "apGeoVersion": "0",
                  "mapType": "0"
              },
              "isPaid": "0",
              "isPlace": "1",
              "isUpdateable": "0",
              "lat": "46.1895583",
              "loginType": "eUnknown",
              "long": "-123.8319473"
          }
      ]
  }


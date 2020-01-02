/* Code for logging an event to SimpleLoggingServerToCsvFile */
/* Inspired by: https://techtutorialsx.com/2016/07/17/esp8266-http-get-requests */

/* https://github.com/esp8266/Arduino */
/* Additional board manager URL: https://arduino.esp8266.com/stable/package_esp8266com_index.json */
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
 
#define MAX_WL_NOT_CONNECTED 3 
 
const char* ssid = "yourNetworkName";
const char* password = "yourNetworkPassword";

/* if DEBUG is defined additional debugging information will be provided on serial */
#define DEBUG
 
void setup () 
{
    /* Counter to count failed WIFI connections */
    int count = 0;
    #ifdef DEBUG
    Serial.begin(115200);
    #endif
    
    WiFi.begin(ssid, password);
 
    while (WiFi.status() != WL_CONNECTED) 
    {
        count++;
        if (count >= MAX_WL_NOT_CONNECTED)
        {
            /* Go to deep sleep until reset */
            ESP.deepSleep(0);
        }
        else
        {
            /* Wait some more */
            delay(1000);
            #ifdef DEBUG
            Serial.print("Connecting - ");
            Serial.println(count);
            #endif
            
        }    
    }
}
 
void loop() 
{
    if (WiFi.status() == WL_CONNECTED) 
    {
        /* Log event to the server */
        HTTPClient http;
         
        http.begin("http://raspberrypi3.local/q67idhrJ56oQj7IElukH");
        int httpCode = http.GET();                                                                
        
        #ifdef DEBUG    
        Serial.println(httpCode); 
        if (httpCode > 0) 
        { 
            String response = http.getString();
            Serial.println(response);
        }
        #endif
        
        /* Close the connection */
        http.end();   
        
    }
    else
    {
        #ifdef DEBUG    
        Serial.println("Not connected!");
        #endif        
    }
    
    /* Go to deep sleep until reset */
    ESP.deepSleep(0);
} 

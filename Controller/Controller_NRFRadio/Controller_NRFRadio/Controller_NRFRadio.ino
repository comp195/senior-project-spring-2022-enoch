#include "SPI.h"
#include "NRFLite.h"

NRFLite _radio;
uint8_t _data = 0;
String ControllerInput;
boolean replay = true;

void setup()
{
    //Communicate on Serial with Baudrate of 115200
    Serial.begin(115200);
    // Set radio to Id = 1, along with the CE and CSN pins
    _radio.init(1, 9, 10);
}

void loop()
{
    if (Serial.available()) 
    {
    ControllerInput = Serial.readStringUntil('\n');
    ControllerInput.trim();
      if (ControllerInput.equals("t")) 
      {
        _data = 0;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("a"))
      {
        _data = 1;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput. equals("s")) 
      {
        _data = 2;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("d")) 
      {
        _data = 3;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("f")) 
      {
        _data = 4;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("w")) 
      {
        _data = 5;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("e")) 
      {
        _data = 6;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("r")) 
      {
        _data = 7;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("i")) 
      {
        _data = 8;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("j")) 
      {
        _data = 9;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("m")) 
      {
        _data = 10;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("k")) 
      {
        _data = 11;
        _radio.send(0, &_data, sizeof(_data));
      }
      else 
      {
        Serial.println("bad ControllerInput");
      }
      

    }

    if (_radio.hasAckData())
    {
       //Acknowledged data's variable
       uint8_t ackData;
       // Reads in acknowledged data
       _radio.readData(&ackData);
       // Prints the acknowledged data
       Serial.println(ackData);
    }
    //Toggle delay for testing purposes
    //delay(1000);
}

#include "SPI.h"
#include "NRFLite.h"

NRFLite _radio;
uint8_t _data = 0;
String ControllerInput;

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
      if (ControllerInput.equals("Forward")) 
      {
        _data = 0;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("Backward")) 
      {
        _data = 1;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("Left")) 
      {
        _data = 2;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("Right")) 
      {
        _data = 3;
        _radio.send(0, &_data, sizeof(_data));
      }
      else if (ControllerInput.equals("EMO")) 
      {
        _data = 4;
        _radio.send(0, &_data, sizeof(_data));
      }
      else 
      {
        Serial.println("bad ControllerInput");
      }

    }
    //Add 1 every time loop occurs (this is for testing purposes)
    //_data++;
    // Send data to the radio with Id = 0
    //_radio.send(0, &_data, sizeof(_data));
    
    //Add 1 every time loop occurs (this is for testing purposes)
    //_data++;
    // Send data to the radio with Id = 0
    _radio.send(0, &_data, sizeof(_data));
    
    //Toggle delay for testing purposes
    //delay(1000);

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

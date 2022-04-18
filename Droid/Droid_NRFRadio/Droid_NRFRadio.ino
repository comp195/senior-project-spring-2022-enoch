#include "SPI.h"
#include "NRFLite.h"

NRFLite _radio;
uint8_t _data;

void setup()
{
    //Communicate on Serial with Baudrate of 115200
    Serial.begin(115200);
    // Set radio to Id = 0, along with its CE and CSN pins
    _radio.init(0, 9, 10);
}

void loop()
{
    //Checks if NRF module has received any data
    if (_radio.hasData())
    {

        //Reads the NRF data
        _radio.readData(&_data);
        //Prints NRF data
        Serial.println(_data);

        //Adds 100 to a newly created Acknowledged data variable
        uint8_t ackData = _data + 100;
        //Sends an acknowledgment message back to the Controller
        _radio.addAckData(&ackData, sizeof(ackData));
    }
}

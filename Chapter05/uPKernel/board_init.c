#include STM32_HAL_H
#include <stdio.h>
#include <string.h>
#include <stdint.h>

#include "py/mphal.h"
#include "py/nlr.h"
#include "py/runtime.h"
#include "pin.h"
#include "genhdr/pins.h"
#include "i2c.h"


#include <stdio.h>
#include <string.h>

#include "py/runtime.h"
#include "py/stackctrl.h"
#include "py/gc.h"
#include "py/mphal.h"
#include "lib/mp-readline/readline.h"
#include "lib/utils/pyexec.h"
#include "lib/oofatfs/ff.h"
#include "extmod/vfs.h"
#include "extmod/vfs_fat.h"


#include "systick.h"
#include "pendsv.h"
#include "pybthread.h"
#include "gccollect.h"
#include "modmachine.h"
#include "i2c.h"
#include "spi.h"
#include "uart.h"
#include "timer.h"
#include "led.h"
#include "pin.h"
#include "extint.h"
#include "usrsw.h"
#include "usb.h"
#include "rtc.h"
#include "storage.h"
#include "sdcard.h"
#include "sdram.h"
#include "rng.h"
#include "accel.h"
#include "servo.h"
#include "dac.h"
#include "can.h"
#include "modnetwork.h"

uint8_t DataRead;

void MyCustom_board_early_init(void)
{
   static HAL_StatusTypeDef Status = HAL_OK;

   // Setup a default GPIO config structure for output pins
   GPIO_InitTypeDef GPIO_InitOutput;
   GPIO_InitOutput.Speed = GPIO_SPEED_HIGH;
   GPIO_InitOutput.Mode = GPIO_MODE_OUTPUT_PP;
   GPIO_InitOutput.Pull = GPIO_PULLUP;

   // Setup a default GPIO config structure for input pins
   GPIO_InitTypeDef GPIO_InitInput;
   GPIO_InitInput.Speed = GPIO_SPEED_HIGH;
   GPIO_InitInput.Mode = GPIO_MODE_INPUT;
   GPIO_InitInput.Pull = GPIO_NOPULL;

   // Setup a default GPIO config structure for analog pins
   GPIO_InitTypeDef GPIO_InitAnalog;
   GPIO_InitAnalog.Speed = GPIO_SPEED_HIGH;
   GPIO_InitAnalog.Mode = GPIO_MODE_ANALOG;
   GPIO_InitAnalog.Pull = GPIO_NOPULL;

   // Enable the clocks on the Arduino headers
   __GPIOA_CLK_ENABLE();
   __GPIOB_CLK_ENABLE();
   __GPIOD_CLK_ENABLE();

   // Set Arduino-D0 High (PA1) then configure the pin
   HAL_GPIO_WritePin(GPIOA, GPIO_PIN_1, GPIO_PIN_SET);
   GPIO_InitOutput.Pin = GPIO_PIN_1;
   HAL_GPIO_Init(GPIOA, &GPIO_InitOutput);

   // Set Arduino-D1 High (PA0) then configure the pin
   HAL_GPIO_WritePin(GPIOA, GPIO_PIN_0, GPIO_PIN_RESET);
   GPIO_InitOutput.Pin = GPIO_PIN_0;
   HAL_GPIO_Init(GPIOA, &GPIO_InitOutput);

   // Set Arduino-D2 High (PD14) then configure the pin
   HAL_GPIO_WritePin(GPIOD, GPIO_PIN_14, GPIO_PIN_SET);
   GPIO_InitOutput.Pin = GPIO_PIN_14;
   HAL_GPIO_Init(GPIOD, &GPIO_InitOutput);

   // Set Arduino-D3 High (PB0) then configure the pin
   HAL_GPIO_WritePin(GPIOB, GPIO_PIN_0, GPIO_PIN_RESET);
   GPIO_InitOutput.Pin = GPIO_PIN_0;
   HAL_GPIO_Init(GPIOB, &GPIO_InitOutput);

   // Set Arduino-D7 (PA4) as an input
   GPIO_InitInput.Pin = GPIO_PIN_4;
   HAL_GPIO_Init(GPIOA, &GPIO_InitInput);

   // Set Arduino-A0 (PC5) as an analog pin
   GPIO_InitAnalog.Pin = GPIO_PIN_0;
   HAL_GPIO_Init(GPIOC, &GPIO_InitAnalog);

//   I2CHandle1.Init.AddressingMode   = I2C_ADDRESSINGMODE_10BIT;
//   I2CHandle1.Init.ClockSpeed      = 400000;
//   I2CHandle1.Init.DualAddressMode = I2C_DUALADDRESS_DISABLED;
//   I2CHandle1.Init.DutyCycle       = I2C_DUTYCYCLE_16_9;
//   I2CHandle1.Init.GeneralCallMode = I2C_GENERALCALL_DISABLED;
//   I2CHandle1.Init.NoStretchMode   = I2C_NOSTRETCH_DISABLED;
//   I2CHandle1.Init.OwnAddress1     = 0xFF;
//   I2CHandle1.Init.OwnAddress2     = 0xfe;


//   i2c_init(&I2CHandle1);

   i2c_init0(); 


   Status = HAL_I2C_IsDeviceReady(&I2CHandle1, 0x38,1, 200);

   printf("Status = %d", Status);

   if(Status == HAL_OK)
   {
      Status = HAL_I2C_Mem_Read(&I2CHandle1, 0x38, 0x12, 1, &DataRead, 2, 200);
   }

   
}


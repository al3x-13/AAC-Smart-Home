# AAC-Smart-Home

## Communication Protocol
In order to make sure data could be transmitted in a standard and stable way between the application and the arduino,
and vice-versa, a protocol was developed.
The protocol was built on top of **UART (Universal Asynchronous Receiver/Transmitter)** interface, 
and it is based on a ***Request/Response* message system** (much like **HTTP**). 
It is a **stateless server-client** protocol, which means the **server** makes a *request* to the **arduino** 
and the later returns with a *response*.

Each **message** send over the protocol has a consistent and predefined format. 
A **message** consists of a text *string*, delimited by a *newline* character (i.e. "**\n**").
Every **message** must have a **CODE** (used to specify which action should be performed) and an optional **DATA** field
(which will sometimes be needed to pass data onto the arduino).

The **message** format is described below.

### Message Format
**`#<CODE>$<DATA>`**
<br>

Below is a diagram describing how the protocol works.

![Communication Protocol](/assets/Smart-Home-Protocol.png)
___

## Datasheet - Communication Protocol Codes

### Server Codes (Requests)
|  Code   | Description                                     | Data                                    | Example Usage |
|:-------:|-------------------------------------------------|-----------------------------------------|:-------------:|
| **P02** | Checks whether the given pin code is correct.   | int - Pin Code                          |  `#P02$3333`  |
| **P03** | Gets current temperature.                       | N/A                                     |    `#P03`     |
| **P04** | Gets current humidity percentage.               | N/A                                     |    `#P04`     |
| **P05** | Gets current lights state.                      | N/A                                     |    `#P05`     |
| **P06** | Sets current lights state.                      | 0 - Lights ON; 1 - Lights OFF           |   `#P06$0`    |
| **P07** | Activates security alarm.                       | N/A                                     |    `#P07`     |
| **P08** | Gets current door button state.                 | N/A                                     |    `#P09`     |
| **P09** | Gets current environment brightness percentage. | N/A                                     |    `#P10`     |
| **P10** | Gets current flames status.                     | N/A                                     |    `#P11`     |
| **P11** | Gets current lights control mode.               | N/A                                     |    `#P11`     |
| **P12** | Sets current lights control mode.               | 0 - App; 1 - Remote                     |   `#P12$1`    |
| **P13** | Sets current lights color.                      | R - Red; G - Green; B - Blue; W - White |   `#P13$B`    |
| **P14** | Activates fire alarm.                           | N/A                                     |    `#P14`     |
| **P15** | Gets current brightness mode.                   | 0 - OFF; 1 - Auto                       |   `#P15$1`    |
| **P16** | Sets current brightness mode.                   | N/A                                     |    `#P16`     |
| **P17** | Gets current brightness level.                  | N/A                                     |    `#P17`     |
| **P18** | Sets current brightness level.                  | int - Brightness Level (20 - 80)        |   `#P18$60`   |
| **P19** | Gets current fire alarm status.                 | N/A                                     |    `#P19`     |
| **P20** | Sets current fire alarm status.                 | 0 - OFF; 1 - Auto                       |   `#P20$0`    |
| **P21** | Gets current brightness control mode.           | N/A                                     |   `#P21$0`    |
| **P22** | Sets current brightness control mode.           | 0 - App; 1 - Potentiometer              |   `#P22$0`    |

### Device Codes (Responses)
|  Code   | Description                                     | Data                                  | Example Usage |
|:-------:|-------------------------------------------------|---------------------------------------|:-------------:|
| **D02** | Returns whether the given pin code is correct.  | 0 - Incorrect; 1 - Correct            |   `#D02$1`    |
| **D03** | Returns current temperature in Celsius.         | float - Temperature                   | `#D03$25.00`  |
| **D04** | Returns current humidity percentage.            | float - Humidity                      | `#D04$31.00`  |
| **D05** | Returns lights state.                           | ON - Lights ON; OFF - Lights OFF      |  `#D05$OFF`   |
| **D06** | Returns whether **P06** was successful.         | 0 - Failure; 1 - Success              |   `#D06$0`    |
| **D07** | Returns whether **P07** was successful.         | 0 - Failure; 1 - Success              |   `#D07$1`    |
| **D08** | Returns current door button state.              | 0 - LOW; 1 - HIGH                     |   `#D09$1`    |
| **D09** | Returns current environment brightness percentage. | int - Brightness                      |   `#D10$23`   |
| **D10** | Returns current flames status.                  | 0 - Not detected; 1 - Flames detected |   `#D11$0`    |
| **D11** | Returns current lights control mode.            | 0 - App; 1 - Remote                   |   `#D11$0`    |
| **D12** | Returns whether **P12** was successful.         | 0 - Failure; 1 - Success              |   `#D12$1`    |
| **D13** | Returns whether **P13** was successful.         | 0 - Failure; 1 - Success              |   `#D13$0`    |
| **D14** | Returns whether **P14** was successful.         | 0 - Failure; 1 - Success              |   `#D14$0`    |
| **D15** | Returns whether **P15** was successful.         | 0 - Failure; 1 - Success              |   `#D15$0`    |
| **D16** | Returns current brightness mode.                | 0 - OFF; 1 - Auto                     |   `#D16$1`    |
| **D17** | Returns current brightness level.               | int - Brightness Level                |   `#D17$30`   |
| **D18** | Returns whether **P18** was successful.         | 0 - Failure; 1 - Success              |   `#D18$1`    |
| **D19** | Returns current fire alarm status.              | 0 - OFF; 1 - Auto                     |   `#D19$1`    |
| **D20** | Returns whether **P20** was successful.         | 0 - Failure; 1 - Success              |   `#D20$0`    |
| **D21** | Returns current brightness control mode.        | 0 - App; 1 - Potentiometer            |   `#D21$1`    |
| **D22** | Returns whether **P22** was successful.         | 0 - Failure; 1 - Success              |   `#D22$1`    |


## Commands
|          Command          | Description                                          |                   Format                    |
|:-------------------------:|------------------------------------------------------|:-------------------------------------------:|
|       **exit/quit**       | Exits program.                                       |                     N/A                     |
|         **help**          | Help menu. List of available commands.               |                     N/A                     |
|         **info**          | General info.                                        |                     N/A                     |
|      **GET lights**       | Returns current lights state.                        |                     N/A                     |
|    **GET temperature**    | Returns current temperature.                         |                     N/A                     |
|     **GET humidity**      | Returns current humidity percentage.                 |                     N/A                     |
|    **GET brightness**     | Returns current brightness percentage.               |                     N/A                     |
|      **GET flames**       | Returns whether flames are currently being detected. |                     N/A                     |
|  **GET firealarmstatus**  | Returns current fire alarm status.                   |                     N/A                     |
|   **GET lightcontrol**    | Returns current light control mode.                  |                     N/A                     |
|  **GET brightnessmode**   | Returns current brightness mode.                     |                     N/A                     |
|  **GET brightnesslevel**  | Returns current brightness mode.                     |                     N/A                     |
| **GET brightnesscontrol** | Returns current brightness control mode.             |                     N/A                     |
|      **SET lights**       | Turns lights ON/OFF.                                 |            `set lights <on/off>`            |
|      **SET lights**       | Sets lights color.                                   |            `set lights <color>`             |
|   **SET lightcontrol**    | Sets lights control mode.                            |       `set lightcontrol <app/remote>`       |
|  **SET brightnessmode**   | Sets brightness mode.                                |       `set brightnessmode <off/auto>`       |
|  **SET brightnesslevel**  | Sets brightness level.                               |        `set brightnesslevel <20-80>`        |
| **SET brightnesscontrol** | Sets brightness control mode.                        | `set brightnesscontrol <app/potentiometer>` |
|  **SET firealarmstatus**  | Sets fire alarm status.                              |      `set firealarmstatus <off/auto>`       |
| **TRIGGER securityalarm** | Triggers security alarm.                             |                     N/A                     |
|   **TRIGGER firealarm**   | Triggers fire alarm.                                 |                     N/A                     |

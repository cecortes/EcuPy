<h1> ZeroW Pi Configuration Files </h1>
<br></br>
<br><ul>
<li>Instalar raspbian en la tarjeta SD por medio de Balena Etcher
<li>Desde Windows abrir el archivo <i>config.txt</i>
<li>Al final del archivo añadir las siguientes líneas:
  <ul><li><b>dtoverlay=dwc
      <li>enable_uart=1</b>
      <br></br>
      <li><b>dtoverlay=mcp2515-can0,oscillator=16000000,interrupt=25
      <li>dtoverlay=spi-bcm2835-overlay</b>
  </ul>
</ul>
<br>Abrir y editar el archivo cmdline.txt agregando:
<ul>
  <li><s>rootwait</s> <b>modules-load=dwc2,g_ether</b>
</ul>
</br>
<br>Conectar el monitor y teclado a la Pi, encenderla y configurarla por medio de:
<ul>
  <li><b>sudo raspi-config</b>
</ul>
</br>
<br>Configurar la ip stática para el usb mediante la edición del archivo:</br>
<ul>
  <li>sudo nano /etc/network/interfaces
</ul>
<h2>
<br>Para tener internet mediante dhcp y realizar la conexión vía wifi, previamente configurada en el wpa_supplicant, El archivo quedaría de la siguiente manera:</br>
</h2>
<i><h5>
<p># interfaces(5) file used by ifup(8) and ifdown(8)
<br>
<p># Please note that this file is written to be used with dhcpcd
<p># For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'
<br>
<p># Include files from /etc/network/interfaces.d:
<p>source-directory /etc/network/interfaces.d
<br>
<p>#allow-hotplug usb0
<p>iface usb0 inet static
<p> address 192.168.10.2
<p> netmask 255.255.255.0
<p> network 192.168.10.0
<p> broadcast 192.168.10.255
<p> gateway 192.168.10.1
<br>
<p>auto wlan0
<p>allow-hotplug wlan0
<p>iface wlan0 inet dhcp
<p>   wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf</i></h5>
<br>
<h2>
<p>Para tener conexión mediante USB, sin conexión por medio de la Wifi, el archivo quedaría de la siguiente manera:
</h2>
<p>
<i><h5>
<p># interfaces(5) file used by ifup(8) and ifdown(8)
<p># Please note that this file is written to be used with dhcpcd</p>
<p># For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'</p>

<p># Include files from /etc/network/interfaces.d:</p>
<p>source-directory /etc/network/interfaces.d</p>

<p>allow-hotplug usb0</p>
<p>iface usb0 inet static</p>
<p>	address 192.168.10.2</p>
<p>	netmask 255.255.255.0</p>
<p>	network 192.168.10.0</p>
<p>	broadcast 192.168.10.255</p>
<p>	gateway 192.168.10.1</p>

<p>#auto wlan0</p>
<p>allow-hotplug wlan0</p>
<p>iface wlan0 inet dhcp</p>
<p>	wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf</p>
</i></h5>
<p>
<p><h2>Para realizar la conexión USB mediante Windows, es necesaria la siguiente configuración de red en el dispositivo RNDIS GADGET:</h2>
<ul>
  <li>Dirección IP: 192.168.10.1
  <li>Máscara de subred: 255.255.255.0
  <li>Puerta de enlace: 192.168.10.1
</ul>
<p>Realizar un ping a la ZeroW con la dirección <i>192.168.10.2</i>
<p>
<p><h2>Para realizar la conexión USB mediante Linux:</h2>
<p>   Mediante terminal, escribir:
<ul><li><i>lsusb</i></ul>
<p>Se mostrará algo como:
<ul><li><i>Netchip Tecnology,Inc Linux-USB Ethernet/RNDIS Gadget</i></ul>
<p>Luego es necesario mostrar los dispositivos de red mediante:
<ul><li><i>ifconfig</ul></i>
<p>Se mostrará un dispositivo "enp1S0" pero el que interesa es "enp0S29f7U1", después de identificarlo es necesario configurar las direcciones de red mediante el terminal:
<ul><li><i>sudo ipconfig <s>enp0s29f7U1</s> 192.168.10.1 netmask 255.255.255.0</i></ul>
<p>
<p><h2>Conexión mediante SSH</h2>
<p><ul><li><i>ssh pi@192.168.10.2</i>
       <li>pwd: 431514
  </ul>
<p>
<p><h2>Configuración del archivo wpa_supplicant</h2>
<p>Editar con nano el archivo:
<ul><li>sudo nano /etc/wpa_supplicant/wpa_supplicant.conf</ul>
<p><i>
<br>ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
<br>update_config=1
<br>country=MX
<p>
<br>network={
<br>  ssid="5P0CKy"
<br>  psk="ZMalqp10"
<br>}
<p>
<br>network={
<br>  ssid="PH0N3"
<br>  psk="ZMalqp10"
<br>}
<p>
<br>network={
<br>  ssid="ZMTdeMEXICO"
<br>  psk="ZMTMexico2878"
<br>}
<p>
<br>network={
<br>  ssid="POPOHUA2"
<br>  psk="ZMalqp10"
<br>}</i>
<br>
<p><h2>Pi Zero W & SPI MCP2551</h2>
<br>
<br><ul>Modificar el archivo /boot/config.txt
      <li><i>sudo nano /boot/config.txt</i>
    </ul>
<br><ul>Descomentar en la sección optional hardware interfaces
      <li><i>dtparam=spi=on</i>
    </ul>
<br><ul>Agregar las siguientes líneas al final del archivo:
      <li><i>dtoverlay=mcp2515-can0,oscillator=16000000,interrupt=25</i>
      <li><i>dtoverlay=spi-bcm2835-overlay</i>
    </ul>
<br>
<p><h2>Instalación CAN UTILS</h2>
<br><ul>Instalar can-utils sobre raspbian:
      <li><i>sudo apt-get install can-utils</i>
    </ul>
<br><ul>Reiniciar la Pi, si la configuración y el cableado son correctos debe de aparece el siguiente directorio:
      <li><i>/sys/bus/spi/devices/spi0.0/net</i>
    </ul>
<br>
<p><h2>Inicio y configuración interface CAN0</h2>
<br><ul>Para iniciar la interface can0 y setup:
      <li><i>sudo ip link set can0 up type can bitrate 500000</i>
    </ul>
<br><ul>Para detener la interface:
      <li><i>sudo ip link set can0 down</i>
    </ul>
<br>
<p><h2>CANDUMP</h2>
<br><ul>Para realizar un dump de los paquetes que circulan por la red CAN
      <li><i>candump -c -c -a can0,#FFFFFFFF</i>
      <li>(Muestra toda la información y el dataframe de cualquier Id)
    </ul>
<br><ul>Para realizar un dump de los paquetes de un Id en específico:
      <li><i>candump -c -c -a can0,100:7FF</i>
      <li>(Muestra el dataframe de el Id 0x100)
    </ul>
<br><ul>Ligas de consulta
      <li><i>https://sgframework.readthedocs.io/en/latest/cantutorial.html</i>
      <li><i>https://manpages.debian.org/testing/can-utils/candump.1.en.html</i>
      <li><i>https://github.com/linux-can/can-utils</i>
    </ul>
<br>
<p><h2>Python CAN</h2>
<br><ul>Instalación:
      <li><i>pip install python-can</i>
    </ul>
<p><h4>Ejemplos de uso:</h4></p>
<p><h3>"CanBusConfig.py"</h3>
  <br>#Importamos la librería
  <br>import can
  <br>
  <br>#Configuración del bus, canal can0 y velocidad 500KBaud
  <br>bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)
</p>
<p><h3>"CanBusListener.py"</h3>
  <br>#Importamos la librería
  <br>import can
  <br>from can import listener
  <br>
  <br>#Configuración del bus, canal can0 y velocidad 500KBaud
  <br>bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)
  <br>
  <br>#Función para imprimir el mensaje CANBUS en pantalla
  <br>def PrintMsg(msg):
  <br>    print(msg)
  <br>
  <br>#Variable que recibe el mensaje para ser usada como argumento
  <br>msg = bus.recv()
  <br>
  <br>#Listener, recibe como argumento el mensaje CANBUS
  <br>listener = PrintMsg(msg)
  <br>
  <br>#listener.stop()
  <br>
  <br>#Usuario
  <br>print(">> Done!!!")
</p>
<p><h3>"CanBusRx.py"</h3>
  <br>#Importamos la librería
  <br>import can
  <br>
  <br>#Configuración del bus, canal can0 y velocidad 500KBaud
  <br>bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)
  <br>
  <br>#Recibe los mensajes del buffer y los muestra en pantalla, de manera ciclíca el pprograma no sale hasta interrupt
  <br>for msg in bus:
  <br>    print(msg)
</p>
<p><h3>"CanBusTx.py"</h3>
  <br>#Importamos la librería
  <br>import can
  <br>from can import Message
  <br>
  <br>#Globales
  <br>'''
  <br>The functional PID query is sent to the vehicle on the CAN bus at ID 7DFh, using 8 data bytes. The bytes are:
  <br>
  <br>                                                            Byte    
  <br>PID Type	        0	        1	                        2	                                        3	    4	    5	    6	    7
  <br>SAE Standard	Number of       Service                     PID code                                    not used (ISO 15765-2 suggests CCh)
  <br>                additional      01 = show current data;     (e.g.: 05 = Engine coolant temperature)	
  <br>                data bytes:     02 = freeze frame;
  <br>                2	
  <br>'''
  <br>arryFuelFrame = bytearray([2, 1, 47, 204, 204, 204, 204, 204])                              #Los valores de la tabla de arriba están convertidos de hex a int
  <br>queryFuelMsg = Message(is_extended_id=False, arbitration_id=2015, data=arryFuelFrame)       #El ID broascast es 7DF en hex y 2015 en int
  <br>
  <br>#Configuración del bus, canal can0 y velocidad 500KBaud
  <br>bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)
  <br>
  <br>#Envío de mensaje CANBUS
  <br>bus.send(queryFuelMsg)
  <br>
  <br>#Detenemos el CANBUS
  <br>bus.shutdown()
  <br>
  <br>#Mostramos el mensaje en pantalla
  <br>print(queryFuelMsg)
</p>
<hr>
<p><h2>CANSNIFFER from can-utils</h2><p>
<hr>
<br><ul>Para realizar una captura de paquetes que circulen en la línea CAN:
      <li><i>cansniffer can0</li>
    </ul>
<hr>
<h1>Envío de datos por medio del CAN BUS</h1>
<hr>
<p>Para enviar un único frame, se utiliza el comando:
  <ul>
    <li>cansend</li>
  </ul>
<p>Ejemplo de uso:
  <ul>
    <li>cansend can0 123#1122334455667788</li>
  </ul>
<p>Para mostrar la ayuda en pantalla:
  <ul>
    <li>cansend -h</li>
  </ul>

<hr>
<h1>PID OBD II</h1>
<hr>
Modes
There are ten modes of operation described in the latest OBD-II standard SAE J1979. They are, the $ prefix indicating a hexadecimal number:

$01. Show current data

$02. Show freeze frame data

$03. Show stored Diagnostic Trouble Codes

$04. Clear Diagnostic Trouble Codes and stored values

$05. Test results, oxygen sensor monitoring (non CAN only)

$06. Test results, other component/system monitoring (Test results, oxygen sensor monitoring for CAN only)

$07. Show pending Diagnostic Trouble Codes (detected during current or last driving cycle)

$08. Control operation of on-board component/system

$09. Request vehicle information

$0A. Permanent DTC’s (Cleared DTC’s)

Vehicle manufactures are not required to support all modes.

Each manufacturer may define additional modes above #9 (e.g.: mode 22 as defined by SAE J2190 for Ford/GM, mode 21 for Toyota) for other information (e.g.: the voltage of the Traction Battery in a HEV).

<hr>
<h1>Standard PIDs</h1>
<hr>

The table below shows the standard OBD-II PIDs as defined by SAE J1979. The expected response for each PID is given, along with information on how to translate the response into meaningful data. Again, not all vehicles will support all PIDs and there can be manufacturer-defined custom PIDs that are not defined in the OBD-II standard.

Note that modes 1 and 2 are basically identical, except that Mode 1 provides current information, whereas Mode 2 provides a snapshot of the same data taken at the point when the last diagnostic trouble code was set. The exceptions are PID 01, which is only available in Mode 1, and PID 02, which is only available in Mode 2. If Mode 2 PID 02 returns zero, then there is no snapshot and all other Mode 2 data is meaningless.

Mode(hex) PID(hex) Data bytes returned Description Min value Max value Units Formula
01 00 4 PIDs supported [01 - 20] Bit encoded [A7..D0] == [PID 0x01..PID 0x20]
01 01 4 Monitor status since DTCs cleared. (Includes malfunction indicator lamp (MIL) status and number of DTCs.) Bit encoded. See below.
01 02 8 Freeze DTC
01 03 2 Fuel system status Bit encoded. See below.
01 04 1 Calculated engine load value 0 100 % A*100/255
01 05 1 Engine coolant temperature -40 215 °C A-40
01 06 1 Short term fuel % trim—Bank 1 -100 (Rich) 99.22 (Lean) % (A-128) * 100/128
01 07 1 Long term fuel % trim—Bank 1 -100 (Rich) 99.22 (Lean) % (A-128) _ 100/128
01 08 1 Short term fuel % trim—Bank 2 -100 (Rich) 99.22 (Lean) % (A-128) _ 100/128
01 09 1 Long term fuel % trim—Bank 2 -100 (Rich) 99.22 (Lean) % (A-128) * 100/128
01 0A 1 Fuel pressure 0 765 kPa (gauge) A*3
01 0B 1 Intake manifold absolute pressure 0 255 kPa (absolute) A
01 0C 2 Engine RPM 0 16,383.75 rpm ((A*256)+B)/4
01 0D 1 Vehicle speed 0 255 km/h A
01 0E 1 Timing advance -64 63.5 ° relative to #1 cylinder A/2 – 64
01 0F 1 Intake air temperature -40 215 °C A-40
01 10 2 MAF air flow rate 0 655.35 g/s ((A*256)+B) / 100
01 11 1 Throttle position 0 100 % A\*100/255
01 12 1 Commanded secondary air status Bit encoded. See below.
01 13 1 Oxygen sensors present [A0..A3] == Bank 1, Sensors 1-4. [A4..A7] == Bank 2…
01 14 2 Bank 1, Sensor 1:Oxygen sensor voltage,
Short term fuel trim

0-100(lean) 1.27599.2(rich) Volts% A _ 0.005(B-128) _ 100/128 (if B==0xFF, sensor is not used in trim calc)
01 15 2 Bank 1, Sensor 2:Oxygen sensor voltage,
Short term fuel trim

0-100(lean) 1.27599.2(rich) Volts% A _ 0.005(B-128) _ 100/128 (if B==0xFF, sensor is not used in trim calc)
01 16 2 Bank 1, Sensor 3:Oxygen sensor voltage,
Short term fuel trim

0-100(lean) 1.27599.2(rich) Volts% A _ 0.005(B-128) _ 100/128 (if B==0xFF, sensor is not used in trim calc)
01 17 2 Bank 1, Sensor 4:Oxygen sensor voltage,
Short term fuel trim

0-100(lean) 1.27599.2(rich) Volts% A _ 0.005(B-128) _ 100/128 (if B==0xFF, sensor is not used in trim calc)
01 18 2 Bank 2, Sensor 1:Oxygen sensor voltage,
Short term fuel trim

0-100(lean) 1.27599.2(rich) Volts% A _ 0.005(B-128) _ 100/128 (if B==0xFF, sensor is not used in trim calc)
01 19 2 Bank 2, Sensor 2:Oxygen sensor voltage,
Short term fuel trim

0-100(lean) 1.27599.2(rich) Volts% A _ 0.005(B-128) _ 100/128 (if B==0xFF, sensor is not used in trim calc)
01 1A 2 Bank 2, Sensor 3:Oxygen sensor voltage,
Short term fuel trim

0-100(lean) 1.27599.2(rich) Volts% A _ 0.005(B-128) _ 100/128 (if B==0xFF, sensor is not used in trim calc)
01 1B 2 Bank 2, Sensor 4:Oxygen sensor voltage,
Short term fuel trim

0-100(lean) 1.27599.2(rich) Volts% A _ 0.005(B-128) _ 100/128 (if B==0xFF, sensor is not used in trim calc)
01 1C 1 OBD standards this vehicle conforms to Bit encoded. See below.
01 1D 1 Oxygen sensors present Similar to PID 13, but [A0..A7] == [B1S1, B1S2, B2S1, B2S2, B3S1, B3S2, B4S1, B4S2]
01 1E 1 Auxiliary input status A0 == Power Take Off (PTO) status (1 == active)[A1..A7] not used
01 1F 2 Run time since engine start 0 65,535 seconds (A*256)+B
01 20 4 PIDs supported 21-40 Bit encoded [A7..D0] == [PID 0x21..PID 0x40]
01 21 2 Distance traveled with malfunction indicator lamp (MIL) on 0 65,535 km (A*256)+B
01 22 2 Fuel Rail Pressure (relative to manifold vacuum) 0 5177.265 kPa (((A*256)+B) * 10) / 128
01 23 2 Fuel Rail Pressure (diesel) 0 655350 kPa (gauge) ((A*256)+B) * 10
01 24 4 O2S1_WR_lambda(1):Equivalence Ratio
Voltage

00 28 N/AV ((A*256)+B)/32768((C*256)+D)/8192
01 25 4 O2S2_WR_lambda(1):Equivalence Ratio
Voltage

00 28 N/AV ((A*256)+B)/32768((C*256)+D)/8192
01 26 4 O2S3_WR_lambda(1):Equivalence Ratio
Voltage

00 28 N/AV ((A*256)+B)/32768((C*256)+D)/8192
01 27 4 O2S4_WR_lambda(1):Equivalence Ratio
Voltage

00 28 N/AV ((A*256)+B)/32768((C*256)+D)/8192
01 28 4 O2S5_WR_lambda(1):Equivalence Ratio
Voltage

00 28 N/AV ((A*256)+B)/32768((C*256)+D)/8192
01 29 4 O2S6_WR_lambda(1):Equivalence Ratio
Voltage

00 28 N/AV ((A*256)+B)/32768((C*256)+D)/8192
01 2A 4 O2S7_WR_lambda(1):Equivalence Ratio
Voltage

00 28 N/AV ((A*256)+B)/32768((C*256)+D)/8192
01 2B 4 O2S8_WR_lambda(1):Equivalence Ratio
Voltage

00 28 N/AV ((A*256)+B)/32768((C*256)+D)/8192
01 2C 1 Commanded EGR 0 100 % 100*A/255
01 2D 1 EGR Error -100 99.22 % (A-128) * 100/128
01 2E 1 Commanded evaporative purge 0 100 % 100*A/255
01 2F 1 Fuel Level Input 0 100 % 100*A/255
01 30 1 # of warm-ups since codes cleared 0 255 N/A A
01 31 2 Distance traveled since codes cleared 0 65,535 km (A*256)+B
01 32 2 Evap. System Vapor Pressure -8,192 8,192 Pa ((A*256)+B)/4 (A is signed)
01 33 1 Barometric pressure 0 255 kPa (Absolute) A
01 34 4 O2S1_WR_lambda(1):Equivalence Ratio
Current

0-128 2128 N/AmA ((A*256)+B)/32768((C*256)+D)/256 – 128
01 35 4 O2S2_WR_lambda(1):Equivalence Ratio
Current

0-128 2128 N/AmA ((A*256)+B)/32768((C*256)+D)/256 – 128
01 36 4 O2S3_WR_lambda(1):Equivalence Ratio
Current

0-128 2128 N/AmA ((A*256)+B)/327685((C*256)+D)/256 – 128
01 37 4 O2S4_WR_lambda(1):Equivalence Ratio
Current

0-128 2128 N/AmA ((A*256)+B)/32768((C*256)+D)/256 – 128
01 38 4 O2S5_WR_lambda(1):Equivalence Ratio
Current

0-128 2128 N/AmA ((A*256)+B)/32768((C*256)+D)/256 – 128
01 39 4 O2S6_WR_lambda(1):Equivalence Ratio
Current

0-128 2128 N/AmA ((A*256)+B)/32768((C*256)+D)/256 – 128
01 3A 4 O2S7_WR_lambda(1):Equivalence Ratio
Current

0-128 2128 N/AmA ((A*256)+B)/32768((C*256)+D)/256 – 128
01 3B 4 O2S8_WR_lambda(1):Equivalence Ratio
Current

0-128 2128 N/AmA ((A*256)+B)/32768((C*256)+D)/256 – 128
01 3C 2 Catalyst TemperatureBank 1, Sensor 1 -40 6,513.5 °C ((A*256)+B)/10 – 40
01 3D 2 Catalyst TemperatureBank 2, Sensor 1 -40 6,513.5 °C ((A*256)+B)/10 – 40
01 3E 2 Catalyst TemperatureBank 1, Sensor 2 -40 6,513.5 °C ((A*256)+B)/10 – 40
01 3F 2 Catalyst TemperatureBank 2, Sensor 2 -40 6,513.5 °C ((A*256)+B)/10 – 40
01 40 4 PIDs supported 41-60 Bit encoded [A7..D0] == [PID 0x41..PID 0x60]
01 41 4 Monitor status this drive cycle Bit encoded. See below.
01 42 2 Control module voltage 0 65.535 V ((A*256)+B)/1000
01 43 2 Absolute load value 0 25,700 % ((A*256)+B)*100/255
01 44 2 Command equivalence ratio 0 2 N/A ((A*256)+B)/32768
01 45 1 Relative throttle position 0 100 % A*100/255
01 46 1 Ambient air temperature -40 215 °C A-40
01 47 1 Absolute throttle position B 0 100 % A*100/255
01 48 1 Absolute throttle position C 0 100 % A*100/255
01 49 1 Accelerator pedal position D 0 100 % A*100/255
01 4A 1 Accelerator pedal position E 0 100 % A*100/255
01 4B 1 Accelerator pedal position F 0 100 % A*100/255
01 4C 1 Commanded throttle actuator 0 100 % A*100/255
01 4D 2 Time run with MIL on 0 65,535 minutes (A*256)+B
01 4E 2 Time since trouble codes cleared 0 65,535 minutes (A*256)+B
01 51 1 Fuel Type From fuel type table see below
01 52 1 Ethanol fuel % 0 100 % A*100/255
01 53 2 Absoulute Evap system Vapour Pressure 0 327675 kpa 1/200 per bit
01 C3 ? ? ? ? ? Returns numerous data, including Drive Condition ID and Engine Speed*
01 C4 ? ? ? ? ? B5 is Engine Idle RequestB6 is Engine Stop Request*
02 02 2 Freeze frame trouble code BCD encoded, See below.
03 N/A n\*6 Request trouble codes 3 codes per message frame, BCD encoded. See below.
04 N/A 0 Clear trouble codes / Malfunction indicator lamp (MIL) / Check engine light Clears all stored trouble codes and turns the MIL off.
05 0100 OBD Monitor IDs supported ($01 – $20)
05 0101 O2 Sensor Monitor Bank 1 Sensor 1 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 0102 O2 Sensor Monitor Bank 1 Sensor 2 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 0103 O2 Sensor Monitor Bank 1 Sensor 3 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 0104 O2 Sensor Monitor Bank 1 Sensor 4 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 0105 O2 Sensor Monitor Bank 2 Sensor 1 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 0106 O2 Sensor Monitor Bank 2 Sensor 2 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 0107 O2 Sensor Monitor Bank 2 Sensor 3 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 0108 O2 Sensor Monitor Bank 2 Sensor 4 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 0109 O2 Sensor Monitor Bank 3 Sensor 1 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 010A O2 Sensor Monitor Bank 3 Sensor 2 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 010B O2 Sensor Monitor Bank 3 Sensor 3 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 010C O2 Sensor Monitor Bank 3 Sensor 4 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 010D O2 Sensor Monitor Bank 4 Sensor 1 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 010E O2 Sensor Monitor Bank 4 Sensor 2 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 010F O2 Sensor Monitor Bank 4 Sensor 3 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 0110 O2 Sensor Monitor Bank 4 Sensor 4 0.00 1.275 Volts 0.005 Rich to lean sensor threshold voltage
05 0201 O2 Sensor Monitor Bank 1 Sensor 1 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 0202 O2 Sensor Monitor Bank 1 Sensor 2 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 0203 O2 Sensor Monitor Bank 1 Sensor 3 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 0204 O2 Sensor Monitor Bank 1 Sensor 4 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 0205 O2 Sensor Monitor Bank 2 Sensor 1 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 0206 O2 Sensor Monitor Bank 2 Sensor 2 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 0207 O2 Sensor Monitor Bank 2 Sensor 3 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 0208 O2 Sensor Monitor Bank 2 Sensor 4 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 0209 O2 Sensor Monitor Bank 3 Sensor 1 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 020A O2 Sensor Monitor Bank 3 Sensor 2 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 020B O2 Sensor Monitor Bank 3 Sensor 3 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 020C O2 Sensor Monitor Bank 3 Sensor 4 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 020D O2 Sensor Monitor Bank 4 Sensor 1 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 020E O2 Sensor Monitor Bank 4 Sensor 2 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 020F O2 Sensor Monitor Bank 4 Sensor 3 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
05 0210 O2 Sensor Monitor Bank 4 Sensor 4 0.00 1.275 Volts 0.005 Lean to Rich sensor threshold voltage
09 00 4 mode 9 supported PIDs 01 to 20 Bit encoded
09 02 5×5 Vehicle identification number (VIN) Returns 5 lines, A is line ordering flag, B-E ASCII coded VIN digits.
09 04 varies calibration ID Returns multiple lines, ASCII coded
09 06 4 calibration

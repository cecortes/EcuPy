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

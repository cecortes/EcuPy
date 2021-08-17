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
<br>Para tener internet mediante dhcp y realizar la conexión vía wifi, previamente configurada en el wpa_supplicant</br>
<p>El archivo quedaría de la siguiente manera:
<br>
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
<p>   wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
<br>
<p>Para tener conexión mediante USB, sin conexión por medio de la Wifi, el archivo quedaría de la siguiente manera:
<p>
<p># interfaces(5) file used by ifup(8) and ifdown(8)
<p>
# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'
</p>

<p># Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d
</p>

<p>allow-hotplug usb0
iface usb0 inet static
	address 192.168.10.2
	netmask 255.255.255.0
	network 192.168.10.0
	broadcast 192.168.10.255
	gateway 192.168.10.1
</p>

<p>#auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
	wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
</p>

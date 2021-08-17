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

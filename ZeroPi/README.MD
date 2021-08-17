<h1> ZeroW Pi Configuration Files </h1>
<br></br>
<br><ul>
<li>Instalar raspbian en la tarjeta SD por medio de Balena Etcher
<li>Desde Windows abrir el archivo <i>config.txt</i>
<li>Al final del archivo añadir las siguientes líneas:
  <ul><li>dtoverlay=dwc
      <li>enable_uart=1
      <br>
      <li>dtoverlay=mcp2515-can0,oscillator=16000000,interrupt=25
      <li>dtoverlay=spi-bcm2835-overlay
  </ul>
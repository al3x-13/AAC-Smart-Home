from controller import SerialController


# Gets current temperature in Celsius
def getTemp(controller: SerialController) -> float:
    controller.sendCommand('#P03')
    return float(controller.receiveCommand('#D03'))


# Sets ideal temperature
def setTemp(controller: SerialController, temp: int) -> bool:
    controller.sendCommand(f"#P08${temp}")
    return


# Gets current humidity percentage
def getHumidity(controller: SerialController) -> float:
    controller.sendCommand('#P04')
    return float(controller.receiveCommand('#D04'))
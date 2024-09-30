from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, RFC, apellidos, nombres):
        self.RFC = RFC
        self.apellidos = apellidos
        self.nombres = nombres

    def mostrar_informacion(self):
        return f"RFC: {self.RFC}, Apellidos: {self.apellidos}, Nombres: {self.nombres}"
    
    @abstractmethod
    def calcular_ingresos(self):
        pass

    @abstractmethod
    def calcular_sueldo_neto(self):
        pass
class EmpleadoVendedor(Empleado):
    def __init__(self, RFC, apellidos, nombres, tasa_comision):
        super().__init__(RFC, apellidos, nombres)
        self.tasa_comision = tasa_comision
        self.monto_ventas = 5
    def calcular_ingresos(self):
        ingresos = self.monto_ventas * self.tasa_comision
        return ingresos
    def calcular_bonificacion(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000:
            return 0
        elif 1000 <= ingresos <= 5000:
            return ingresos * 0.05
        else:
            return ingresos * 0.1
    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000:
            return ingresos * 0.11
        else:
            return ingresos * 0.15
    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        bonificaciones = self.calcular_bonificacion()
        descuentos = self.calcular_descuento()
        sueldo_neto = ingresos + bonificaciones - descuentos
        if sueldo_neto  < 150:
            raise ValueError("El sueldo neto no puede ser menor a 150")
        return sueldo_neto
class EmpleadoPermanente(Empleado):
    def __init__(self, RFC, apellidos, nombres, sueldo_base, num_seguro_social):
        super().__init__(RFC, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.num_seguro_social = num_seguro_social
    def recalcular_sueldo_base(self, aumento):
        self.sueldo_base += aumento
    def calcular_descuento_seguro(self):
        return self.sueldo_base * 0.11
    def calcular_ingresos(self):
        return self.sueldo_base
    def calcular_sueldo_neto(self):
        descuento = self.calcular_descuento_seguro()
        sueldo_neto = self.sueldo_base - descuento
        if sueldo_neto < 150:
            raise ValueError("El sueldo neto no puede ser menor a 150")
        return sueldo_neto
empleados = [
    EmpleadoVendedor("empleado_j34", "Tapia Lopez", "Jiovani Asael", 500),
    EmpleadoPermanente("empleado_j34", "Tapia", "Asael",500 , "123456789")]
for empleado in empleados:
    print(empleado.mostrar_informacion())
    print(f"Sueldo Neto: {empleado.calcular_sueldo_neto()}")

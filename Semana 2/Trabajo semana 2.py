# ============================================
#          CLASE BASE: Dispositivo
# ============================================

class Dispositivo:
    """
    ABSTRACCIÓN:
    Representa un dispositivo inteligente genérico.
    Solo contiene lo mínimo necesario para describirlo:
    nombre, estado y consumo eléctrico(espero que funcione).
    """
#Me base en los comentarios que tenia el ejemplo ya que antes no habia programado en python pero espero acostumbrarme

    def __init__(self, nombre, consumo):
        # ENCAPSULACIÓN: Atributos protegidos
        self._nombre = nombre
        self._encendido = False
        self._consumo = consumo  # watts

    # ----------------- Encapsulación -----------------
    @property
    def consumo(self):
        return self._consumo

    @consumo.setter
    def consumo(self, valor):
        if valor >= 0:
            self._consumo = valor

    # Método general
    def activar(self):
        self._encendido = True

    def desactivar(self):
        self._encendido = False

    def info(self):
        estado = "Encendido" if self._encendido else "Apagado"
        return f"{self._nombre} - {estado} - Consumo: {self._consumo}W"


# ============================================
#               HERENCIA: Luz
# ============================================

class Luz(Dispositivo):
    """
    Luz inteligente que hereda de Dispositivo.
    Agrega el atributo brillo.
    """

    def __init__(self, nombre, consumo, brillo):
        super().__init__(nombre, consumo)
        self._brillo = brillo  # porcentaje

    # POLIMORFISMO: redefinimos info()
    def info(self):
        estado = "Encendida" if self._encendido else "Apagada"
        return (f"Luz {self._nombre} - {estado} - "
                f"Brillo: {self._brillo}% - "
                f"Consumo: {self._consumo}W")


# ============================================
#             HERENCIA: Termostato
# ============================================

class Termostato(Dispositivo):
    """
    Termostato inteligente que hereda de Dispositivo.
    Agrega la temperatura configurada.
    """

    def __init__(self, nombre, consumo, temperatura):
        super().__init__(nombre, consumo)
        self._temperatura = temperatura

    # POLIMORFISMO nuevamente aplicado
    def info(self):
        estado = "Activo" if self._encendido else "Inactivo"
        return (f"Termostato {self._nombre} - {estado} - "
                f"Temperatura: {self._temperatura}°C - "
                f"Consumo: {self._consumo}W")


# ============================================
#               PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":
    d1 = Dispositivo("Lampara de nombre generico no se me ocurre nada", 5)
    l1 = Luz("Lámpara Sala", 12, 80)
    t1 = Termostato("TermoCentral", 30, 22)

    d1.activar()
    l1.activar()
    t1.activar()

    print(d1.info())
    print(l1.info())   # Polimorfismo
    print(t1.info())   # Polimorfismo

    # Encapsulación: modificamos el consumo de forma controlada
    l1.consumo = 15
    print("Nuevo consumo de la luz:", l1.consumo)

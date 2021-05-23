class Calculator:
    def pow(self, a, b):
    # modulo a ser testado
        if b < 0:
            raise ValueError("exponent must be postive")
        if b == 0:
            return 1
        result = a
        for i in range(1, b):
            result = result * a
        return result

class Calculator: # Coberto pelo teste
    def pow(self, a, b): # Coberto pelo teste
        # modulo a ser testado
        if b < 0: # Coberto pelo teste
            raise ValueError
        if b == 0: # Coberto pelo teste
            return 1
        result = a #
        for i in range(1, b): # Coberto pelo teste
            result = result * a # Coberto pelo teste
        return result # Coberto pelo teste

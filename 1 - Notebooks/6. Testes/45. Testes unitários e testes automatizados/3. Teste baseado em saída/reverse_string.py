def reverse_string(string):
    # modulo a ser testado
    reversed_string = ""
    for i in range(len(string), 0, -1):
        reversed_string += string[i-1]
    return reversed_string

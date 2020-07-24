import sys


def init():
    # print(sys.argv)

    try:
        lim_sup: float = float(sys.argv[1])
    except IndexError:
        lim_sup: float = float(input("Límite superior: "))
    except ValueError:
        print(f"Límite superior debe ser un número, introduciste '{sys.argv[1]}'")
        return

    try:
        lim_inf: float = float(sys.argv[2])
    except IndexError:
        lim_inf: float = float(input("Límite inferior: "))
    except ValueError:
        print(f"Límite inferior debe ser un número, introduciste '{sys.argv[2]}'")
        return

    try:
        obj: float = float(sys.argv[3])
    except IndexError:
        obj: float = float(input("Objetivo: "))
    except ValueError:
        print(f"Objetivo debe ser un número, introduciste '{sys.argv[3]}'")
        return

    try:
        err: float = float(sys.argv[4])
    except IndexError:
        err: float = float(input("Error: "))
    except ValueError:
        print(f"Error debe ser un número, introduciste '{sys.argv[4]}'")
        return

    return punto_medio(lim_sup, lim_inf, obj, err)


def punto_medio(lim_sup: float, lim_inf: float, obj: float, err: float = 0.05) -> float:
    p: float = lim_sup
    r: float = lim_inf
    q: float = (lim_sup + lim_inf) / 2

    i: int = 0
    res: float = 0

    min: float = obj - err
    max: float = obj + err

    while (q > max or q < min) or q != obj:
        q = (p + r) / 2
        i += 1

        if q == obj:
            break

        dif_sup = abs(q - max)
        dif_inf = abs(q - min)

        if dif_sup < dif_inf:
            p = q
        else:
            r = q

    res = q
    return [res, i]


if __name__ == "__main__":
    # resultado, iteraciones = init()
    resultado, iteraciones = punto_medio(100, 20, 52.5, 0.05)
    print(f"Resultado: {resultado} | Iteraciones: {iteraciones}")

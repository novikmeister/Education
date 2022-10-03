class Seryi_tsvet:
    def __init__(self):
        pass

    def izm_contrast(self, z, A):
        z = A * z
        if len(z.shape) > 1:
            for i in range(z.shape[0]):
                for j in range(z.shape[1]):
                    if z[i][j] < 0:
                        z[i][j] = 0
                    elif z[i][j] > 255:
                        z[i][j] = 255
                    else:
                        z[i][j] = z[i][j]
        else:
            for i in range(len(z)):
                if z[i] < 0:
                    z[i] = 0
                elif z[i] > 255:
                    z[i] = 255
                else:
                    z[i] = z[i]
        return z

    def izm_yarkost(self, z, B):
        z = z + B
        if len(z.shape) > 1:
            for i in range(z.shape[0]):
                for j in range(z.shape[1]):
                    if z[i][j] < 0:
                        z[i][j] = 0
                    elif z[i][j] > 255:
                        z[i][j] = 255
                    else:
                        z[i][j] = z[i][j]
        else:
            for i in range(len(z)):
                if z[i] < 0:
                    z[i] = 0
                elif z[i] > 255:
                    z[i] = 255
                else:
                    z[i] = z[i]
        return z

    def izm_contrast_and_yarkost(self, z, A, B):
        z = A * z + B
        if len(z.shape) > 1:
            for i in range(z.shape[0]):
                for j in range(z.shape[1]):
                    if z[i][j] < 0:
                        z[i][j] = 0
                    elif z[i][j] > 255:
                        z[i][j] = 255
                    else:
                        z[i][j] = z[i][j]
        else:
            for i in range(len(z)):
                if z[i] < 0:
                    z[i] = 0
                elif z[i] > 255:
                    z[i] = 255
                else:
                    z[i] = z[i]
        return z

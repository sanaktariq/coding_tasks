import numpy as np
import matplotlib.pyplot as plt

def circle_segment(res, i, radius):
    return np.array([np.cos(((2 * np.pi) / res) * i) * radius,
                     np.sin(((2 * np.pi) / res) * i) * radius])

def circle(radius, res=50):
    return np.array([circle_segment(res, i, radius) for i in range(0, res + 1)])

cir_result = circle(50, res=50)
#print(cir_result)
#print(cir_result[:, 0], cir_result[:, 1])

print(cir_result.tolist())
res1 = [[50.0, 0.0], [49.60573506572389, 6.266661678215213], [48.429158056431554, 12.43449435824274], [46.48882429441257, 18.4062276342339], [43.81533400219318, 24.087683705085766], [40.45084971874737, 29.389262614623657], [36.448431371070576, 34.22735529643444], [31.87119948743448, 38.525662138789464], [26.791339748949834, 42.216396275100756], [21.288964578253633, 45.241352623300976], [15.450849718747373, 47.552825814757675], [9.369065729286225, 49.114362536434435], [3.1395259764656647, 49.901336421413575], [-3.13952597646567, 49.901336421413575], [-9.369065729286241, 49.11436253643443], [-15.450849718747378, 47.552825814757675], [-21.288964578253637, 45.241352623300976], [-26.791339748949838, 42.21639627510075], [-31.87119948743448, 38.525662138789464], [-36.44843137107058, 34.227355296434425], [-40.450849718747364, 29.38926261462366], [-43.81533400219318, 24.08768370508576], [-46.488824294412574, 18.406227634233886], [-48.429158056431554, 12.43449435824274], [-49.60573506572389, 6.266661678215205], [-50.0, -1.6081226496766367e-14], [-49.60573506572389, -6.266661678215216], [-48.429158056431554, -12.43449435824275], [-46.48882429441256, -18.406227634233918], [-43.815334002193175, -24.08768370508577], [-40.450849718747364, -29.389262614623668], [-36.448431371070576, -34.22735529643444], [-31.87119948743448, -38.52566213878947], [-26.791339748949817, -42.21639627510076], [-21.28896457825361, -45.24135262330099], [-15.450849718747378, -47.552825814757675], [-9.369065729286232, -49.114362536434435], [-3.13952597646566, -49.901336421413575], [3.139525976465686, -49.901336421413575], [9.369065729286257, -49.11436253643443], [15.450849718747362, -47.55282581475768], [21.288964578253633, -45.241352623300976], [26.791339748949834, -42.216396275100756], [31.8711994874345, -38.52566213878945], [36.4484313710706, -34.22735529643441], [40.45084971874739, -29.38926261462363], [43.81533400219318, -24.087683705085766], [46.488824294412574, -18.40622763423389], [48.42915805643156, -12.434494358242725], [49.60573506572389, -6.266661678215189], [50.0, 3.2162452993532734e-14]]
print(cir_result.tolist() == res1)


#result = (cir_result[:, 0], cir_result[:, 1])
#print(result)

#plt.plot(cir_result[:, 0], cir_result[:, 1])
#print("cir_result[:, 0], cir_result[:, 1]")
#plt.show()

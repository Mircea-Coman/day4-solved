import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar, bracket

def objective_f(A, y_exp, y_model):
    s = np.sum((y_exp - A*y_model)**2, axis = 0)
    return s

experimental_data = np.load('I_q_IPA_exp.npy')
mask = ~np.logical_or(np.isnan(experimental_data[:, 1]), np.isnan(experimental_data[:, 0])) # remove nans
experimental_data = experimental_data[mask, :]

model_data = np.load('I_q_IPA_model.npy')

interp_f = interp1d(model_data[:, 0], model_data[:, 1], kind = 'linear')

model_interpolated = np.empty_like(experimental_data)
model_interpolated[:, 0] = experimental_data[:, 0]
model_interpolated[:, 1] = interp_f(experimental_data[:, 0])

# print(model_interpolated[:, 0] - experimental_data[:, 0])

fit = minimize_scalar(objective_f, bracket=(1E-3, 1E-4, 0),  args=(experimental_data[:, 1], model_interpolated[:, 1]))

model_fit = np.empty_like(experimental_data)
model_fit[:, 0] = experimental_data[:, 0]
model_fit[:, 1] = fit.x*model_interpolated[:, 1]

plt.figure(figsize = (13, 8))
plt.plot(experimental_data[:, 0], experimental_data[:, 1], 'k-', label = 'Experimental')
plt.plot(model_data[:, 0], model_data[:, 1]*1E-4, 'o-', label = r'Model Original $\times 10^{-4}$')
# plt.plot(model_interpolated[:, 0], model_interpolated[:, 1]*1E-4, '.', label = 'Model Interpolated $\times 10^{-4}$')
plt.plot(model_fit[:, 0], model_fit[:, 1], 'r-', label = f'Model Fit (Scaling factor: {fit.x:.2E})')

# plt.yscale('log')
plt.legend()
plt.xlabel('Scattering Vector')
plt.ylabel('Scattering Strength')

plt.show()

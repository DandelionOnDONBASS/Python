import printing_functioms
import funcion
from funcion import greet_user
from funcion import greet_user as gu
import pizza as piz
from pizza import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron','robor bobot']
completed_models = []
printing_functioms.print_models(unprinted_designs,completed_models)
printing_functioms.show_completed_models(completed_models)

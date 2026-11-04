
import sys
import os
# Add project root (parent directory) to Python's search path for imports
# Step-by-step:
# 1. os.path.dirname(__file__) -> Gets the directory of this current script
# 2. os.path.join(..., "..")   -> Moves up one level to the parent directory
# 3. os.path.abspath(...)       -> Normalizes it into an absolute path
# 4. sys.path.append(...)       -> Allows importing modules from that parent folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Modules.ecommerce.shopping import sales
# print(dir(sales))
# print(sales.__name__) # ecommerce.shopping.sales
# print(sales.__package__) # ecommerce.shopping
# print(sales.__file__) # /Users/harvinaregladoarisga/Desktop/Python Fundamentals/ecommerce/shopping/sales.py


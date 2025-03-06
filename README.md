# 🚀 Django API Performance Lab

**Django API Performance Lab** is an experimental Django application designed for testing API performance optimizations in Django REST Framework (DRF).  
This repository explores:
- 📌 Optimizing database queries using `select_related()` and `only()`
- 📌 Reducing Django serialization overhead
- 📌 Caching API responses with Redis
- 📌 Reducing JSON response size for faster client-side processing
- 📌 Using pagination for large datasets

## ⚡ Features & Experiments
This repository contains a Django project with an API endpoint for `Person` objects, including related profiles (`Profile`, `ProfileB`, `ProfileC`). The main goal is to measure and optimize response times.

### 🔹 **Optimization Techniques**
1. **Database Query Optimization**  
   - Using `select_related()` to minimize queries  
   - Using `only()` to fetch only necessary fields  
   - Comparing `values()` vs `ModelSerializer`  

2. **Serialization Improvements**  
   - Replacing `ModelSerializer` with `SerializerMethodField`  
   - Converting QuerySet to dictionaries with `values()`  
   - Benchmarking DRF's serialization time  

3. **Caching with Redis**  
   - Implementing `cache.get()` and `cache.set()` for API responses  
   - Deleting cache upon `POST` requests  
   - Checking performance improvements with caching  

4. **Reducing JSON Overhead**  
   - Measuring JSON size with `sys.getsizeof(data)`  
   - Enabling `GZipMiddleware` for compressed responses  
   - Removing unnecessary nested fields  

5. **Pagination for Large Datasets**  
   - Setting `PAGE_SIZE=100` to avoid sending massive responses  
   - Enabling Django REST Framework pagination  

## 🚀 How to Run the Project
### 1️⃣ **Clone the repository**
```sh
git clone https://github.com/michalprzyl/django-optimalization-redis
```


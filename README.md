# Aplikasi-Pengingat-Pembayaran-UKT-dan-Deadline-Tugas
aplikasi web sederhana untuk membantu mahasiswa mengelola pengingat pembayaran UKT dan deadline tugas dalam satu tempat. Fitur utama: autentikasi sederhana (login), dashboard berisi daftar pembayaran dan tugas, penambahan pengingat, penghapusan, dan notifikasi sederhana (penjadwalan opsional).

1. Deskripsi Singkat Sistem
Proyek ini adalah sebuah aplikasi web sederhana yang terdiri dari:
Halaman Login
Halaman Home/Dashboard
Sistem autentikasi sederhana menggunakan session
Tampilan web menggunakan HTML + CSS
Aplikasi ini dibuat sebagai bagian dari tugas mata kuliah, dengan tujuan memahami dasar implementasi sistem login, routing server, serta struktur proyek backend–frontend.

2. Teknologi yang Digunakan
Backend
Python 3.x
Flask (routing, session, template rendering)
Frontend
HTML
CSS (custom)
Tools
Visual Studio Code
Git & GitHub Repository

3. Jika ingin menjalankan:
Install Flask
pip install flask
Jalankan server
python Backend.py
Buka browser
http://127.0.0.1:5000/
Username dummy: admin
Password dummy: 123

4. Bagian yang Dibantu Generative AI

Beberapa bagian dibuat dengan bantuan AI untuk mempercepat pekerjaan, namun tetap dipahami dan disesuaikan:

Contoh bagian yang dibantu AI:

a. Struktur awal Flask:
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret123"
b. Fungsi login dasar:
if username == "admin" and password == "123":
    session["user"] = username
    return redirect("/home")
c. Template HTML dasar (login.html):
<form method="POST">
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <button type="submit">Login</button>
</form>
d. Saran layout folder & style CSS

Semua kode kemudian diadaptasi, dirapikan, dan disesuaikan dengan kebutuhan tugas.




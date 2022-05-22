#!/usr/bin/env python3
import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html")
print()
print("""<link rel="stylesheet" href="/static/style.css">""")
print("<h1>TV Shows</h1>")

shows = [
    ["Death Note", 10],
    ["Accel World", 8],
    ["Future Diary", 6.5]
]

print("<table>")
print(" <thead>")
print("     <tr>")
print("         <th>Show Name</th>")
print("         <th>Rating (/10)</th>")
print("     </tr>")
print(" </thead>")
print(" <tbody>")
for show_name, rating in shows:
    print(" <tr>")
    print(f"     <td>{show_name}</td>")
    print(f"     <td>{rating}</td>")
    print(" </tr>")
print("     <tr>")
print(" </tbody>")
print("</table>")
# Killer-Queen-CTF-2021_Writeups
 - Xem qua mã nguồn thì chúng ta biết được đó là một đoạn bytecode python
 - Chúng ta có thể tham khảo tại: https://www.beyondjava.net/java-programmers-guide-java-byte-code và https://dzone.com/articles/introduction-to-java-bytecode
 ![image](https://user-images.githubusercontent.com/57956165/139803348-829e646c-5d3f-4ca8-a94d-c29776be7a34.png)
   + Chuỗi "rwhxi}eomr\\^`Y" sẽ lưu vào biến a, chuỗi "f]XdThbQd^TYL&\x13g" lưu vào biến z
   + 2 chuỗi này cộng lại và lưu vào biến a: a="rwhxi}eomr\\^`Yf]XdThbQd^TYL&\x13g"
- Các dòng bytecode tiếp theo chúng ta sẽ phân tích chúng thành các mã python. Kết quả sẽ lưu vào biến f.
![image](https://user-images.githubusercontent.com/57956165/139804023-2d00a07d-53d5-46d2-afb8-ef9df8073063.png)

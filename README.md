[![License: MIT](https://black.readthedocs.io/en/stable/_static/license.svg)](https://github.com/psf/black/blob/main/LICENSE)

# javfuscate
Obfuscate java program source code

Turn:
```java
class HelloWorld{
	public static void main(String[] args){
		System.out.println("Hello World");
		int loop = 3;
		for(int i = 0; i < loop; i++){
			System.out.println(i);
		}
	}
}
 ```

Into:
 ```
\u0063\u006c\u0061\u0073\u0073 \u0048\u0065\u006c\u006c\u006f\u0057\u006f\u0072\u006c\u0064{
	\u0070\u0075\u0062\u006c\u0069\u0063 \u0073\u0074\u0061\u0074\u0069\u0063 \u0076\u006f\u0069\u0064 \u006d\u0061\u0069\u006e(\u0053\u0074\u0072\u0069\u006e\u0067[] \u0061\u0072\u0067\u0073){
		\u0053\u0079s\u0074\u0065\u006d.\u006f\u0075\u0074.p\u0072\u0069\u006e\u0074\u006cn("\u0048\u0065\u006c\u006c\u006f \u0057\u006f\u0072\u006c\u0064");
		\u0069\u006e\u0074 \u006co\u006f\u0070 = \u0033;
		\u0066\u006f\u0072(\u0069n\u0074 \u0069 = \u0030; i < \u006c\u006f\u006f\u0070; \u0069++){
			S\u0079\u0073\u0074\u0065\u006d.\u006f\u0075\u0074.p\u0072\u0069n\u0074\u006cn(\u0069);
		}
	}
}
 ```


FAQ:
---------------------  
Q Does this compile?  
A It does. The Java compiler decodes the unicode first and it becomes a vaild program again.  
  
Q Why would I want to do this?  
A You don't.  
  
Q Are there any advantages to doing this?  
A No, unless your goal is to create unreadable code.  
  
Q Why don't you convert all the characters in the program?  
A I like it being a mix of both. It keeps the program structure, but still makes it impossible to read.  

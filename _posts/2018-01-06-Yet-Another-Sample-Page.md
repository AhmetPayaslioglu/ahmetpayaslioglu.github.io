---
title: Ses Dosyası’nın İçerisine Yazı Gizleme | Steganography
published: true
---

Değerli okuyucular Merhaba. Ben Ahmet Payaslıoğlu. Bu yazıda Steganography yöntemiyle “Ses Dosyası’nın İçerisine Yazı Gizleme konusuna değineceğim.Öncelikle Steganography’den bahsetmek istiyorum.Steganografi, eski Yunanca’da “gizlenmiş yazı” anlamına gelir ve bilgiyi gizleme (önemli: şifreleme değil) bilimine verilen addır. Steganografi’nin şifrelemeye göre en büyük avantajı bilgiyi gören bir kimsenin gördüğü şeyin içinde önemli bir bilgi olduğunu fark edemiyor olmasıdır, böylece içinde bir bilgi aramaz (oysaki bir şifreli mesaj, çözmesi zor olsa bile, gizemi dolayısıyla ilgi çeker).Steganography’nin bir çok çeşidi vardır. Bu yazıda ses dosyasının içerisine yazı gizlemeyi deneyeceğim. Sonrasında bu ses dosyasını analiz ederek , gizlenmiş yazıyı bulacağız.Tarihte steganografi, hem şifreleme öncesi dönemde hem de sonrasında (ilgi çekmeme avantajından dolayı) kullanılmıştır.
*  Eski Yunanistan’da, insanlar mesajları tahtaya yazıp üzerini mumla kaplarlardı. Böylece cisim kullanılmamış bir tablete benzerdi öte yandan mumun eritilmesiyle birlikte içindeki gizli mesaj okunabilirdi.
*  Herodot’un bir hikâyesine göre Pers saldırısının öncesinde saçları tıraşlanan bir kölenin kafasına yazılan uyarı mesajı, saçlarının uzaması sayesinde saklanmıştır. Bu sayede, mesaj dikkat çekmeden gerekli yere ulaşabilmiş, ulaştığında da kölenin saçları tekrar kesilerek uyarı okunabilmiştir.
*  II. Dünya Savaşı sırasında, New York’taki, Japon millî ajanı (Velvalee Dickinson) oyuncak bebek pazarlamacısı kılığı altında saklanmaktaydı. Bu ajan, Amerikan ordusunun hareketlerini bebek siparişi içeren mektuplar içine saklayarak Güney Amerika’daki adreslere gönderiyordu.
*  Özellikle 1960’larda mor ötesi boya ile yazı yazabilen sprey ve kalemler moda idi. Bu kalemlerin yazdığı yazılar, sadece bir mor ötesi ışıkla görülebiliyordu.

# [](#header-1)Ses Dosyasının İçerisine Yazıyı Gizleme

Bu işlemi yapmak için Coagula programını kullanacağız. Programı açtıktan sonra , öncelikle File > New Image‘yi seçtikten sonra yükseklik ve genişlik ayarlarından ekranı büyütüyoruz.
<img src="https://miro.medium.com/max/2400/0*po07Ifv6vKpLAnOp.png" alt="">
<p>Sonrasında siyah ekrana mouse yardımıyla istediğiniz yazıyı yazabilirsiniz.</p>
<img src="https://miro.medium.com/max/2400/0*iSRuOj_Mru6Vet1P.png" alt="">
<p>Ok işareti ile gösterdiğim kutucuğa tıkladığımızda , yazının sese dönüştüğünü duyabilirsiniz.</p>
<img src="https://miro.medium.com/max/2400/0*V8vKVurWItW06C5y.png" alt="">
<p>Yazıyı başarıyla ses dosyasının içerisine gömdük. Kaydetmek için File > Save Sound As seçeneğine tıklayalım. Dosyayı .wav uzantılı kaydettiğini görebilirsiniz. Bildiğiniz üzere .wav uzasıntısı ses dosyasını temsil ediyor. Şimdi bu dosyayı nasıl analiz edebiliriz buna bakalım.</p>


## [](#header-2)Ses Dosyasın İçerisine Gizlenmiş Yazıyı Analiz Etme

<p>Bunun için Sonic Visualiser programını kullanacağız. Kendi işletim sisteminize uygun olanı indirdikten sonra , uygulamayı açalım.</p>
<p>Uygulamayı açtıktan sonra , kaydettiğimiz ses dosyasını File>Open seçeneğinden seçelim.</p>
### [](#header-3)Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### [](#header-4)Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### [](#header-5)Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### [](#header-6)Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:



### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![](https://assets-cdn.github.com/images/icons/emoji/octocat.png)

### Large image

![](https://guides.github.com/activities/hello-world/branching.png)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```

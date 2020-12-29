---
title: Ses Dosyası’nın İçerisine Yazı Gizleme | Steganography
published: true
---

Bu yazımda Steganography yöntemiyle “Ses Dosyası’nın İçerisine Yazı Gizleme konusuna değineceğim.Öncelikle <a style="color:red;">Steganography’den</a> bahsetmek istiyorum.Steganografi, eski Yunanca’da “gizlenmiş yazı” anlamına gelir ve bilgiyi gizleme (önemli: şifreleme değil) bilimine verilen addır. Steganografi’nin şifrelemeye göre en büyük avantajı bilgiyi gören bir kimsenin gördüğü şeyin içinde önemli bir bilgi olduğunu fark edemiyor olmasıdır, böylece içinde bir bilgi aramaz (oysaki bir şifreli mesaj, çözmesi zor olsa bile, gizemi dolayısıyla ilgi çeker).Steganography’nin bir çok çeşidi vardır. Bu yazıda ses dosyasının içerisine yazı gizlemeyi deneyeceğim. Sonrasında bu ses dosyasını analiz ederek , gizlenmiş yazıyı bulacağız.Tarihte steganografi, hem şifreleme öncesi dönemde hem de sonrasında (ilgi çekmeme avantajından dolayı) kullanılmıştır.
*  Eski Yunanistan’da, insanlar mesajları tahtaya yazıp üzerini mumla kaplarlardı. Böylece cisim kullanılmamış bir tablete benzerdi öte yandan mumun eritilmesiyle birlikte içindeki gizli mesaj okunabilirdi.
*  Herodot’un bir hikâyesine göre Pers saldırısının öncesinde saçları tıraşlanan bir kölenin kafasına yazılan uyarı mesajı, saçlarının uzaması sayesinde saklanmıştır. Bu sayede, mesaj dikkat çekmeden gerekli yere ulaşabilmiş, ulaştığında da kölenin saçları tekrar kesilerek uyarı okunabilmiştir.
*  II. Dünya Savaşı sırasında, New York’taki, Japon millî ajanı (Velvalee Dickinson) oyuncak bebek pazarlamacısı kılığı altında saklanmaktaydı. Bu ajan, Amerikan ordusunun hareketlerini bebek siparişi içeren mektuplar içine saklayarak Güney Amerika’daki adreslere gönderiyordu.
*  Özellikle 1960’larda mor ötesi boya ile yazı yazabilen sprey ve kalemler moda idi. Bu kalemlerin yazdığı yazılar, sadece bir mor ötesi ışıkla görülebiliyordu.

# [](#header-1)Ses Dosyasının İçerisine Yazıyı Gizleme

Bu işlemi yapmak için Coagula programını kullanacağız. Programı açtıktan sonra , öncelikle <strong>File</strong> > <strong>New Image</strong>‘yi seçtikten sonra yükseklik ve genişlik ayarlarından ekranı büyütüyoruz.
<img src="https://miro.medium.com/max/2400/0*po07Ifv6vKpLAnOp.png" alt="">
<p>Sonrasında siyah ekrana mouse yardımıyla istediğiniz yazıyı yazabilirsiniz.</p>
<img src="https://miro.medium.com/max/2400/0*iSRuOj_Mru6Vet1P.png" alt="">
<p>Ok işareti ile gösterdiğim kutucuğa tıkladığımızda , yazının sese dönüştüğünü duyabilirsiniz.</p>
<img src="https://miro.medium.com/max/2400/0*V8vKVurWItW06C5y.png" alt="">
<p>Yazıyı başarıyla ses dosyasının içerisine gömdük. Kaydetmek için File > Save Sound As seçeneğine tıklayalım. Dosyayı .wav uzantılı kaydettiğini görebilirsiniz. Bildiğiniz üzere .wav uzasıntısı ses dosyasını temsil ediyor. Şimdi bu dosyayı nasıl analiz edebiliriz buna bakalım.</p>


## [](#header-2)Ses Dosyasın İçerisine Gizlenmiş Yazıyı Analiz Etme

<p>Bunun için Sonic Visualiser programını kullanacağız. Kendi işletim sisteminize uygun olanı indirdikten sonra , uygulamayı açalım.</p>
<p>Uygulamayı açtıktan sonra , kaydettiğimiz ses dosyasını File>Open seçeneğinden seçelim.</p>
<img src="https://miro.medium.com/max/2400/0*6FU7l01Q83RmC5nU.png" alt="">
<p>Seçtiğimiz dosya karşımıza bu şekilde gelecektir.</p>
<img src="https://miro.medium.com/max/2400/0*ROneDsmo98BatPlF.png" alt="">
<p>Frekanslar sıkışık olduğundan dolayı mouse’un scroll’unu yukarıya doğru döndermeliyiz. Bu sayede frekanslar genişleyecektir.</p>
<img src="https://miro.medium.com/max/2400/0*RXczXQjQzbSswFQD.png" alt="">
<p>Sonrasında gizlenmiş yazıyı analiz etmek için Sağ tık > Layer > Add Spectogram seçeneğine basıyoruz.</p>
<img src="https://miro.medium.com/max/2400/0*ApiTvmfeZ1cISreW.png" alt="">
<p>Sonrasında karşımıza gizlediğimiz yazı geliyor :) </p>
<img src="https://miro.medium.com/max/2400/0*IDXGvHZP7b8jImVk.png" alt="">
<p>Steganography yönteminin bir çeşidi olan Ses Dosyası’nın İçerisine Yazı Gizleme yöntemi ile yazımızı gizledikten sonra , tekrardan ses dosyasını analiz ederek , gizlenmiş yazıyı tespit ettik.</p>



### [](#header-3)Kaynaklar
* https://tr.wikipedia.org/wiki/Steganografi
* https://yusufcancakircs.blogspot.com/2020/08/yaziyi-ses-dosyasinda-gizleme-steganography.html

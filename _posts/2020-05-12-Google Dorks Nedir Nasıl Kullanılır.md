---
title: Google Dorks Nedir? Nasıl Kullanılır?

published: true
---
<p>Bu yazıda sizlere Google Dorks ‘un ne olduğunu ve nasıl kullanıldığını göstereceğim.</p>
<p>Bu seri 2 kısımdan oluşacak. İlk bölümün amacı normal kullanıcılar için Google Dorks’un nasıl kullanıldığını ve basit sorgular yaparak günlük hayattaki araştırmalarına hız kazandırmak için olacaktır. İkinci bölümde ise daha çok hackerlerin hangi sorgular yaparak Google Dorks’tan bilgiler edindiğini anlatacağım. İlk bölüme başlayalım.</p>


# [](#header-1)Google Dorks Örnekleri

<a style="color:red;">site</a>
<p>örnek -> site:sibertehdit.com</p>
<p>Bu arama sözcüğünü kullandığımız zaman sadece o siteye ait sayfalar gelir.</p>
<img src="https://miro.medium.com/max/700/1*pPpjrpim9QMIJPaDw3y4SQ.png" alt="">

<a style="color:red;">site</a>
<p>örnek -> site:sibertehdit.com</p>
<p>Bu arama sözcüğünü kullandığımız zaman sadece o siteye ait sayfalar gelir.</p>
<img src="https://miro.medium.com/max/700/1*pPpjrpim9QMIJPaDw3y4SQ.png" alt="">

<a style="color:red;">intext</a>
<p>Örnek -> intext:sibertehdit</p>
<p>İçerisinde sibertehdit kelimesinin geçtiği websitelerini bulur.</p>
<img src="https://miro.medium.com/max/700/1*OunInVF8RjxOLpmaiv9omg.png" alt="">

<a style="color:red;">intitle</a>
<p>Örnek-> intitle:sibertehdit</p>
<p>Bu sorgu, yalnızca sayfaların başlıklarında “sibertehdit” terimlerini içeren sayfaları getirir.</p>
<img src="https://miro.medium.com/max/700/1*VTG8CW0qQPZu0t8wBqjBtQ.png" alt="">

<a style="color:red;">inurl</a>
<p>Örnek-> inurl:sibertehdit</p>
<p>Bu sorgu belirtilen terimi url’de arar.</p>
<img src="https://miro.medium.com/max/2400/1*ESgJfBr3uEdo375QuhAfxA.png" alt="">

<a style="color:red;">filetype</a>
<p>örnek -> filetype:pdf</p>
<p>Bu sorgu , aradığınız terimin hangi tipte olduğunu belirtir (pdf,docx,txt,jpg gibi). Örnek olarak ben pentest alanındaki pdf’leri aramak istiyorsam bu sorguyu şöyle kullanabilirim : pentest filetype:pdf</p>
<img src="https://miro.medium.com/max/700/1*iY2c5wU5aaRyOOxtng1DIg.png" alt="">

<a style="color:red;">cache</a>
<p>örnek -> cache:sibertehdit.com</p>
<p>Bu sorgu , geçerli sayfanın yerine web sayfasının önbelleğe alınmış halini getirir.</p>
<img src="https://miro.medium.com/max/700/1*IWXu2tyy1cYW2ug_efWRjQ.png" alt="">

<a style="color:red;">related</a>
<p>örnek -> related:thehackernews.com</p>
<p>Thehackernews sayfasına benzer websitelerini arar.</p>
<img src="https://miro.medium.com/max/700/1*sHKVXX6a9vdA9RlREZR8oA.png" alt="">

<a style="color:red;">=? operatörü</a>
<p>örnek-> 1 bitcoin=?usd</p>
<p>=? operatörü bize sol tarafdaki değerin , sağ tarafdaki değer bazında kaç olduğunu getirir. Örnek olarak 1 bitcoin kaç dolar diye sormuş oldum.</p>
<img src="https://miro.medium.com/max/700/1*VlGn4lVG-xWmKwbtsaV4UA.png" alt="">

<p>Bazı sorguları inceledik . Daha bir sürü sorgu olduğu için geriye kalan sorgulardan birazını aşağıda listelemek istiyorum.</p>

# [](#header-2)Diğer Örnekler:
* <a style="color:red;">Url </a>: İnternet’te bir kaynağa (belge veya resim gibi) rastgelen, standart bir formata uygun bir karakter dizgisidir.
* <a style="color:red;">allintext</a> : Aradığımız tüm text dosyalarını bulacaktır.
* <a style="color:red;">link</a> : Aradığımız link’e ait sayfaları bulacaktır
* <a style="color:red;">inanchor</a> : Google aradığımız içerik bilgisi ile bağlantılı, içeriklere sahip bağlantılar ile aramamızı kısıtlayacaktır.
* <a style="color:red;">numrange</a> : Google aradığımız numara veya numara aralıklarını bulacaktır.
* <a style="color:red;">daterange</a> : Aradığımız tarih veya tarih aralıklarını bulacaktır.
* <a style="color:red;">author</a> : Aradığımız yazara ait bilgileri bulacaktır.
* <a style="color:red;">groups</a> : Google aradığımız bir topluluk ismini google groups da bulunan makaleler ve benzer isimdeki topluluk içerikleri ile sınırlandıracaktır.
* <a style="color:red;">insubject</a> : Google, konuyla belirttiğimiz terimleri içeren içerikler(makale vb.) ile sınırlar.
* <a style="color:red;">msgid</a> : (message id yani Türkçe adı ile mesaj kimliği) Her e-postanın bir kimliği(id) vardır.Google da bu kimlik ile arama yaptığımızda bu e-posta ile bağlantılı bilgiler ile aramamız sınırlanacaktır.
* <a style="color:red;">define</a> : Aradığımız girdi ile ilgili bilgi bulacaktır.
* <a style="color:red;">maps</a> : Aradığımız lokasyon ile ilgili bilgi bulacaktır.
* <a style="color:red;">book</a> : Aradığımız kitap ile ilgili bilgi bulacaktır.
* <a style="color:red;">info</a> : Google girdiğimiz url ile ilgili web sayfası hakkında bilgiler ile aramayı sınırlayacaktır.
<p>İlk bölümün sonuna geldik . İkinci bölümde Hackerlerin Google Dorku nasıl kullanarak bazı kritik bilgiler elde ettiğini inceleyeceğiz. 🙂</p>

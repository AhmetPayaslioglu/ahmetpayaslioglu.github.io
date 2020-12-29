---
title: Silinen Verileri Kurtarma

published: true
---

<p>Bugün silinen verileri nasıl geri kurtarabiliriz biraz inceleyelim. Yazının başında sizlere biraz teorik bilgi verdikten sonra uygulamaya geçeceğim. Örnek bir seneryo düşünürsek bazı fotoğraflarınızı veya dökümanlarınızı bilerek veya bilmeyerek silmiş olabilirsiniz. Ya da başka bir seneryo üzerinden hareket edersek bir delil incelemek için herhangi bir disk içerisinde önceden silinmiş verileri geri kurtararak inceleme yapabilirsiniz. Biz bu yazıda bilerek silinmiş pdf ve jpeg uzantılı 2 tane veriyi geri getireceğiz. Sonrasında bu verileri geri getirememek için neler yapabiliriz yani antiforensic işlemi nasıl olur , verileri tamamen nasıl silebiliriz , kanıtları tamamen nasıl yok edebiliriz onlara değineceğim .</p>
<p>Öncelikle silinen verilerimizi geri getirmek için veri kazıma işlemi yapmamız gerekiyor. Bugün bu işlemi yapmak için Forensic katagorisinde olan Foremost aracını kullanacağız. Yazıya başlamadan söylemek isterim ki %100 verilerinizi geri getirmenizi kimse garanti edemez. Fakat bazı kriterlere uyuyorsanız silinen verilerinizin bir kısmını geri getirebilirsiniz. Bu kriterlere biraz değinmek istiyorum. Bildiğiniz üzere veriler 1 ve 0 lardan oluşur. Disk üzerinde bir şeyler sildiğiniz de o veriler aslında silinmez. O verilerin silinmesi için üzerine yeni verilerin eklenmesi gerekir. Yani kaba tabiriyle altta kalanın canı çıksın olur. Siz disk üzerine veri yazdıkça eski verilerinizi geri getirme şansınız o kadar düşer. Eğer bir delili tamamen silmek istiyorsanız bu mantık üzerinden yola çıkarak wipe işlemi yapmanız gerekiyor. Nedir bu wipe ? Yazının devamında anlatacağım.Bu dediğim işlemlerin hepsine yazının devamında göz atacağız. Şimdi biraz uygulamaya geçelim.</p>

# [](#header-1) Silinen Verileri Geri Kurtarma

<p>Öncelikle flash diskimizin içerisinin boş olduğuna ve verilerimizin silindiğine emin olalalım . Sonrasında önceden içerisinde olan jpeg ve pdf dosyamızı geri getirmeye çalışalım. Silinen verileri geri kurtarma ‘ya başlayalım.</p>
<img src="https://miro.medium.com/max/2400/1*g-Nx-rx7W3zeadLlOahhdQ.png" alt="">
<p>Sonrasında verilerimizi kurtarmak için Foremost aracımızı indirelim.</p>



## [](#header-2)apt-get install foremost
<img src="https://miro.medium.com/max/607/1*L8umvl4ZlemnWkObrkZebg.png" alt="">
<p>Sonrasında bu aracın hangi parametlerle çalıştığına bir göz atalım.</p>


### [](#header-3)foremost -h
<img src="https://miro.medium.com/max/700/1*jFtxdNa5Oz8BwwSCI8enCg.png" alt="">
<p>Yukarıda gördüğünüz bazı parametleri açıklamak istiyorum</p>

*  -v tararken bize ayrıntılı bilgi verir
*  -q hızlı modda tarama yapar
*  -t ile alınacak dosya türünü belirtebiliriz örnek ( pdf,jpeg,docx,png)
*  -o ile bu verileri hangi dosyaya çıkartmak istediğimizi belirtiriz
<p>Şimdi de hangi disk üzerinden veri kurtarma yapacağımıza bakmamız için fdisk -l komutunu yazıyoruz . Bu komut mevcut disklerinizi görüntüleyecektir . Ben flash disk üzerindeki silinmiş bir kaç veriyi geri getireceğim. Aşağıdaki fotoğrafta gördüğünüz üzere benim flash diskim /dev/sdb olarak gözüküyor</p>
<img src="https://miro.medium.com/max/700/1*mC19pLQfgCy-ExpkpJYSwg.jpeg" alt="">


<p>Diskimizin isminide öğrendiğimize göre artık veri kazıma işlemine başlayabiliriz.</p>
<p>foremost -v -q -t jpeg,pdf -o ahmetpayas /dev/sdb komutunu yazarak veri kurtarma işlemini başlatıyorum. Bu işlem geri getirmek istediğiniz verilerin boyutuna göre zaman değişkenliği gösterebilir.</p>
<img src="https://miro.medium.com/max/700/1*mC19pLQfgCy-ExpkpJYSwg.jpeg" alt="">
<p>şlem bittikten sonra 1 adet pdf dosyası ve 1 adet jpg dosyasını geri getirdiğini söyledi. Yazının başında zaten bu verileri geri getirmek istediğimi ve bunları bilerek sildiğimi belirtmiştim. Yani amacımıza ulaştık.</p>
<img src="https://miro.medium.com/max/2400/1*KluWxWvkS0oMI7_Ei7_8fQ.png" alt="">
<p>Şimdi verilerimizi kontrol edelim bir problem veya eksiklik var mı diye.
ahmetpayas dizinine gidiyorum. 3 tane dosya ile karşılaşıyorum.
1.si audit.txt = geri getirmeye çalıştığımız veri kazıma sürecindeki ayrıntılı bilgileri veriyor.
2.si jpg klasörü
3.sü pdf klasörü
Öncelikle jpg dosyamı kontrol ediyorum. display (dosya adı) komutuyla resmimi açıyorum. Aşağıdaki fotoğrafta gördüğünüz gibi problemsiz bir şekilde veriyi geri getirdik.
</p>
<img src="https://miro.medium.com/max/2400/1*PVTqtxVoy0p4rSd4GchhCw.png" alt="">

##### [](#header-5)Header 4

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

```

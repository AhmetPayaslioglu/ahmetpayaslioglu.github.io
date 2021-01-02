---
title: Docker Nedir ? Docker Kurulumu ve Konfigürasyonu Nasıl Yapılır?

published: true
---

<p>Son yıllarda Docker ismini çok sık duymaya başladık. Bir çok yazılım projesinde docker kullanılmaya başlandı. Bu yazın Big Data Teknolojileri üzerine bir şirkette staj yaptım. Günümüzde Docker gibi teknolojilerin ne kadar önemli olduğunu ve kullanıldığını o zaman anladım. Bu fikirden yola çıkarak Docker Teknolojisini sizlere elimden geldiğince aktarmak istiyorum. Bu yazımda Docker Nedir ? Dockerın faydaları , kurulumu ve gerekli konfigürasyonlarından bahsedeceğim. Bu yazıdan sonra Docker üzerine Pentest araçlarının nasıl kurulduğuna dair bir yazı daha hazırlayacağım. Öncelikle Docker Teknolojisini tanıyalım ve gerekli kurumları, konfigürasyonları yapalım. Yazıma başlamadan önce şunu belirtmek isterimki , Sanallaştırma Teknolojileri kullananlar için (VirtualBox, Vmware vb.) kasma sorunları ve yetersiz donanımlara sahip arkadaşlar için , alternatif olarak kullanacakları bu teknoloji onlara ilaç gibi gelecektir 🙂 Ben bu yazımda Docker’in üzerine UBUNTU kurulumunu göstereceğim. Siz istediğiniz bir imajı kurabilirsiniz. Keyifli okumalar dilerim.</p>
<p>Docker, yazılım geliştiriciler ve sistemciler için geliştirilen açık kaynaklı bir sanallaştırma platformudur.
Docker ile Linux, Windows ve MacOSX üzerinde Linux ve Windows sanal containerler (makineler) çalıştırabilirsiniz.Bu platform sayesinde web sistemlerinin kurulumunu, testini ve dağıtımını kolaylıkla gerçekleştirebilirsiniz.</p>

# [](#header-1) Docker’ın Avantajları

* Kullanımı kolay
* Esneklik
* İzole ortam sağlar
* Yazılım tanımlı ağı destekler
* Hızlı dağıtım
* Güvenlik

<p>Dockerin faydalarına göz atarsak Docker’ın sanallaştırma yapısı, bilinen sanal makinelerden (VirtualBox, Vmware vb) farklı olarak bir Hypervisor katmanına sahip değildir. Bunun yerine Docker Engine üzerinden, konak işletim sistemine erişmekte ve sistem araçlarını paylaşımlı kullanmaktadır. Böylece klasik VM’lere göre daha az sistem kaynağı tüketmektedir.</p>
<p>Docker, LXC sanallaştırma mekanizması üzerine kurulu. Bir Docker imajı, container denilen birimlerde çalıştırılıyor. Her bir container bir süreç (process) kullanıyor.</p>
<p>Bir makinada gücüne bağlı olarak binlerce docker containerı birden çalışabilir. Container imajları ortak olan sistem dosyalarını paylaşıyorlar. Dolayısıyla disk alanından tasarruf ediliyor. Uygulama containerları ortak bin(exe) ve kütüphaneleri kullanıyorlar. Ancak klasik sanal makine sistemlerinde her bir uygulama için ayrı işletim sistemi ve kütüphane dosyaları ayrılmak zorunda. Bu yüzden klasik sanal makinalar için daha güçlü sistemlere ve donanımlara ihtiyacınız olabilir. Fakat Docker’de öyle bir ihtiyacınız yok.</p>
<p>Aşağıdaki resimden Docker’in nasıl bir mimariye sahip olduğunu daha net bir şekilde anlayabiliriz.</p>
<img src="https://miro.medium.com/max/2400/0*-fdS5rF4bnMinXdY.png" alt="">
<p>Yukarıdaki şemada da görüleceği üzere Docker(Container Mimarisi) uygulama ile işletim sistemi (OS) arasında yer alır. Docker üzerinde bulunduğu işletim sistemini birden fazla container ile paylaşır. Docker, uygulamanızı kaynakların yeterli olduğu herhangi bir makinede çalıştırılabilecek bir yeniden kullanılabilir modül olarak sunar. Bu sayede VM’den farklı olarak, daha iyi ayarlanmış bir kaynak yönetimine izin verir ve boşa harcanan cpu veya ram kaynağı miktarını en aza indirir.</p>

## [](#header-2) Docker Kurulumu Ve Kullanımı
<p>Docker’ı kurmak için Linux terminalini açmanız ve aşağıdaki komutu yazmanız yeterlidir:</p>
<a style="color:red;">apt install docker.io</a>
<img src="https://miro.medium.com/max/700/0*EgBdsK61597uJszs.png" alt="">
<p>Sürümü kontrol etmek için aşağıdaki komutu kullanabilirsiniz </p>
<a style="color:red;">docker –version</a>
<p>Ayrıca, docker’ın hizmetinizde sunduğu tüm seçenekleri bilmek için docker’da help komutunu çalıştırabilirsiniz.</p>
<a style="color:red;">docker –help</a>



### [](#header-3)foremost -h

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
<p>İşlem bittikten sonra 1 adet pdf dosyası ve 1 adet jpg dosyasını geri getirdiğini söyledi. Yazının başında zaten bu verileri geri getirmek istediğimi ve bunları bilerek sildiğimi belirtmiştim. Yani amacımıza ulaştık.</p>
<img src="https://miro.medium.com/max/2400/1*KluWxWvkS0oMI7_Ei7_8fQ.png" alt="">
<p>Şimdi verilerimizi kontrol edelim bir problem veya eksiklik var mı diye.
ahmetpayas dizinine gidiyorum. 3 tane dosya ile karşılaşıyorum.
1.si audit.txt = geri getirmeye çalıştığımız veri kazıma sürecindeki ayrıntılı bilgileri veriyor.
2.si jpg klasörü
3.sü pdf klasörü
Öncelikle jpg dosyamı kontrol ediyorum. display (dosya adı) komutuyla resmimi açıyorum. Aşağıdaki fotoğrafta gördüğünüz gibi problemsiz bir şekilde veriyi geri getirdik.
</p>
<img src="https://miro.medium.com/max/2400/1*PVTqtxVoy0p4rSd4GchhCw.png" alt="">
<p>Sonrasında pdf klasörümüze bir göz atalım . Pdf dosyamı açmak için xdg-open (dosya adı) komutunu kullanıyorum. Aşağıdaki resimde gördüğünüz gibi pdf dosyamda sorunsuz bir şekilde geri getirildi.</p>
<img src="https://miro.medium.com/max/2400/1*mJwiucuw8kO_1CvCAwIYWg.png" alt="">


##### [](#header-5)Verileri Kalıcı Olarak Silme İşlemi

<p>Gördüğünüz gibi istediğim verileri geri getirmiş oldum. Şimdi bu verileri ne yapsaydık geri getiremezdik ondan bahsetmek istiyorum . Silinen verileri nasıl geri kurtarma işlemi yapamayız biraz da onlara değineceğim . Yazının başında biraz bahsetmiştim . Wipe işlemi yapılan disklerdeki verileri geri kurtaramayız. Wipe dediğimiz kavram verinin üzerinde binlerce yeni veri ekleyerek eski verileriniz tamamen yokolmasına yol açar. Peki nasıl wipe yaparız diyorsanız , wipe işlemi için bazı araçlar var fakat en basitinden windows -> biçimlendir yaparak wipe edebilirsiniz. Dikkat edin genelde hızlı biçimlendirme kutucuğu dolu olarak gelir. O kutucuktaki tik işaretini kaldırmanız gerekiyor. Sonrasında biçimlendirme işlemini başlatabilirsiniz. Bu işlem uzun sürecektir çünkü diskinizin üzerine binlerce veri yazılıp silinecektir. Aşağıdaki resimde gördüğünüz işlemi yaparsanız verileriniz bir daha geri getirilmemek üzere yok olur . Antiforensic işlemi diyebiliriz. Delilleri böylece yokedebilirsiniz.</p>
<img src="https://miro.medium.com/max/239/1*EPyJUczhSoVNCBJBCTrvOg.png" alt="">
<p>Bir yazımın daha sonuna geldik . Yukarıda belirttiğim işlemleri silinen verilerinizi geri getirmek için faydalı olarak kullanabilirsiniz. Verilerinizi tamamen nasıl ortadan kaldırabileceğinize de değindim .Bir sonraki yazımda görüşmek üzere 🙂</p>




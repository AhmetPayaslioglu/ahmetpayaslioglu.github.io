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
<p><img src="https://miro.medium.com/max/700/0*EgBdsK61597uJszs.png" alt=""></p>
<p>Sürümü kontrol etmek için aşağıdaki komutu kullanabilirsiniz </p>
<a style="color:red;">docker –version</a>
<p>Ayrıca, docker’ın hizmetinizde sunduğu tüm seçenekleri bilmek için docker’da help komutunu çalıştırabilirsiniz.</p>
<a style="color:red;">docker –help</a>
<p><img src="https://miro.medium.com/max/700/0*kR-_ExTSLaYyEILr.png" alt=""></p>
<p>Docker açılıp çalışmaya başladığında, docker konteynerinizdeki herhangi bir imajı çalıştırabilir veya çekebilirsiniz. Örneğin, burada Hello World’u çalıştırmayı deniyoruz . Aşağıdaki komutu çalıştırdığınızda, öncelikle yerel deponuzu kontrol edecektir; görüntü orada yoksa docker hub‘dan çekecektir.</p>
<p><a style="color:red;">docker run hello-world</a></p>
<img src="https://miro.medium.com/max/692/0*FpU_BBCPnwUQ-zv0.png" alt="">




### [](#header-3)Docker Üzerine Ubuntu Kurulumu


<p>Docker , komut satırı gibi çalıştığı için (CLI) bu nedenle doğrudan terminalden istediğiniz herhangi bir imajı arayabilirsiniz. Mesela, burada Ubuntu’yu aradık. Burada dikkat edilmesi gereken bir husus var. Yıldızı fazla olan imajın , orijinal olma ihtimalı daha yüksektir. Ubuntu imajını aramak için aşağıdaki komutu yazıyoruz.</p>

<p><a style="color:red;">docker search ubuntu</a></p>
<img src="https://miro.medium.com/max/700/0*B1fJ81FSzMzHXuY2.png" alt="">
<p>İmajı bulduğunuzda, aşağıdaki komutla onu konteynırınıza çekebilirsiniz:</p>

<p><a style="color:red;">docker pull ubuntu</a></p>
<img src="https://miro.medium.com/max/667/0*rR3k2GPTVziK_MbH.png" alt="">
<p>Şimdi docker’ınızda kaç tane imajımızın olduğunu kontrol etmek için aşağıdaki komutu yazmalıyız.</p>
<p><a style="color:red;">docker images</a></p>
<img src="https://miro.medium.com/max/700/0*3p0Se3cdI1NKCHXK.png" alt="">
<p>Herhangi bir imajı kaldırmak için aşağıdaki komutu kullanabilirsiniz.</p>
<p><a style="color:red;">docker rmi hello-world</a></p>
<img src="https://miro.medium.com/max/700/0*CQOkYYD7NuGqo0I5.png" alt="">
<p>Yukarida verdiğim rmi komutu imajı kaldırmayı ifade eder. İmajı kaldırdıktan sonra tekrardan <p><a style="color:red;">docker images</a></p> yazdığımızda hello-world’un kaldırılmış olduğunu görüyoruz.</p>
<img src="https://miro.medium.com/max/700/0*xULxHBbn2LYtHk7_.png" alt="">
<p>Şimdi, ps komutunun verdiği detaylarda, ubuntu imajlarımızın isminin her imaj için docker tarafından üretilen rastgele bir isim olan <a style="color:red;">adoring curie</a> olduğunu görebilirsiniz . Bu adı yeniden adlandırmak için aşağıdaki komutu kullanabiliriz. İsmini <a style="color:red;">ignite</a> olarak değiştirdikten sonra tekrar kontrol etmek için <a style="color:red;">docker ps</a> komutunu kullanıyoruz. Aşağıda gördüğünüz gibi isim değişmiş durumda.</p>
<p><a style="color:red;">docker run -it -d ubuntu</a></p>
<p><a style="color:red;">docker run -it -d –name “ignite” ubuntu</a></p>
<p><a style="color:red;">docker ps</a></p>
<img src="https://miro.medium.com/max/700/0*44nPGg_yoZJIHxzB.png" alt="" >
<p>Çalışan konteynerı etkileşimli hale getirmek için <a style="color:red;">attach</a> komutu kullanılır</p>
<p><a style="color:red;">docker attach ignite</a></p>
<img src="https://miro.medium.com/max/636/0*Dt-YlqmHXc3g_puc.png" alt="" >
<p>Ps komutunu kullanarak docker’da çalışan tüm işlemleri görebiliriz.</p>
<p><a style="color:red;">docker ps</a></p>
<p><a style="color:red;">docker ps -a</a></p>
<img src="https://miro.medium.com/max/700/0*Lqc_jzaRUawIvkDa.png" alt="" >
<p>Çalışan konteyneri durdurduktan sonra kaldırmak için aşağıdaki görüntüdeki gibi stop komutundan sonra rm komutunu kullanabilirsiniz. proses komutu yardımı ile durup durmadığını kontrol edebilirsiniz.</p>
<p><a style="color:red;">docker rm ignitedocker</a></p>
<p><a style="color:red;">docker stop <.docker-container> </a></p>
<p><a style="color:red;">ps -a</a></p>
<img src="https://miro.medium.com/max/700/0*zB1s_lkhAIUKHiB3.png" alt="" >

#### [](#header-4)Docker İmajlarını Dışarıya Aktarabiliriz



<p>Docker dosya sistemini bir arşiv olarak dışa aktarabiliyoruz. Bir docker konteynerinin dosya sistemini tar olarak sıkıştırmak için <a style="color:red;">export</a> komutunu kullanabiliriz. Dockerimizin anlık görüntüsünü dışarıya aktarabiliriz. Ben kendi sistemimdeki bir yere <a style="color:red;">siberdocker.gz </a> olarak export ettim. ls komutu yaparak kaydedilip kaydedilmediğini kontrol edebilirsiniz. Aşağıdaki görüldüğü gibi ls komutunu yazdığımda <a style="color:red;">siberdocker.gz </a> dosyası karşıma geliyor. Yani başarılı bir şekilde export ettik.</p>
<img src="https://miro.medium.com/max/700/0*VoVHU6II8VJKO64V.png" alt="" >

<p>Konteyneri tar dosyası olarak dışa aktardığınızda, dosyanın hash değeri şu şekilde olabilir. Bu hash değerini görüntülemek için şu komutu giriyoruz.</p>
<p><a style="color:red;">cat {path} |docker import — siberlab</a></p>
<img src="https://miro.medium.com/max/700/0*I5ihdwiDn9XrdQaD.png" alt="" >
<p>Başka bir docker üzerine yükleyebileceğiniz konteyner imajını kaydetmek için save komutunu kullanabilirsiniz. Daha sonra bu “kaydedilmiş” görüntüleri yeni bir docker üzerine yükleyebilir ve bu imajı çalıştırabilirsiniz.</p>
<p><a style="color:red;">docker save <.container name> | gzip > {path for tar} siberdocker.gz</a></p>
<p><a style="color:red;">docker load -i /{path}/siberdocker.gz</a></p>
<img src="https://miro.medium.com/max/700/0*ZwJMFuX6GaTA59iz.png" alt="" >
<p>En sonda yukarıdaki fotoğrafta görüldüğü üzere docker imajını , en son olarak docker images diyerek yüklenip yüklenmediğini kontrol edebiliriz. Yukarıdaki fotoğrafta gördüğümüz üzere siberlab başarıyla yüklenmiş.</p>
<p>Bir yazımın daha sonuna geldim. Farklı bir yazıda görüşmek üzere 🙂 </p>
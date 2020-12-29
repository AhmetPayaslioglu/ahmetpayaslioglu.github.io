---
title: PE(Portable Executable) Dosya Formatı Üzerinden Malware Analizi
published: true
---

<p>Bu yazımda PE Dosya formatı üzeriden nasıl malware analizi yapabileceğimizi anlattım. Kali Linux üzerinden trojen oluşturduktan sonra, oluşturduğumuz bu trojeni farklı ortamlarda analiz edeceğiz. PE dosyaları üzerinden , bu yazılımın zararlı olup olmadığına dair ipuçları elde edeceğiz.</p>
<p>Portable Executable (kısaca PE), Windows’ un çalıştırılabilir dosya formatıdır. Dosya formatları , programların fonksiyonlarla alakalı bir takım bilgileri analiz yapan kişiye sunabilmektedir. PE dosya formatı Windows executable ve DLL dosyaları tarafından kullanılabilmektedir. PE dosyaları başlık bilgileri ile başlar ve bu başlık bilgileri program için gereken kütüphane fonksiyonlarını uygulama tipleri gibi bilgileri içermektedir.</p>
<p>Bağlı kütüphaneler ve fonksiyonlardan yararlanılarak analiz için bilgiler edilebilir. PE dosya başlığı program tarafından yüklenen kütüphane ve fonksiyonlar ile alakalı bilgileri tutar.</p>

# [](#header-1)DLL Dosyaları Ne İşe Yarıyor?

<p>Windows işletim sisteminde programların sorunsuz bir şekilde çalışabilmek için ihtiyaç duyduğu öncelikli dosyalar, “yürütülür dosya” veya “program dosyası” denilen dosyalardır. Yürütülür dosyalar, “.exe” uzantılı dosyalardır.</p>
<p>Örneğin; iexplore.exe dosyası, Internet Explorer tarayıcısını başlatmanızı sağlayan yürütülebilir dosyadır.</p>
<p>Dll dosyaları ise Windows işletim sistemine ait programlar için birer fonksiyon kütüphanesidir. Programlar bu kütüphaneleri gerektiğinde kullanarak programlandıkları işleri yerine getirirler. Eğer kullandığınız programların ihtiyaç duyduğu dll dosyaları (dinamik bağlantı kütüphaneleri) eksikse ya da hasarlıysa “Dll dosyası bulunamadı“, “Dll dosyası hasarlı ya da eksik” gibi hatalar ile karşılaşırsınız.</p>
<p>Şimdi Kali Linux üzeriden msfvenom aracı ile trojen oluşturalım.</p>
<img src="https://miro.medium.com/max/2400/0*34MCZaWez0iDw69A.png" alt="">
<p>Oluşturduğumuz bu trojeni Dependency Walker programı ile analiz edeceğim.</p>




## [](#header-2)Dependency Walker

<p>Oluşturduğum trojeni Dependency Walker programı ile açıyorum.</p>
<p>Karşıma bir takım DLL dosyaları geldi. DLL dosyalarını incelediğimizde ağ bağlantısı için WS2_32.DLL yi kullandığını gördüm.</p>
<img src="https://miro.medium.com/max/2400/0*uZJtWVCjr0A4hxEH.png" alt="">
<p>Sonrasında DLL’leri biraz daha inceledikten sonra , şifreli bağlantı için CRYPT32.DLL kullandığını farkediyorum.</p>
<img src="https://miro.medium.com/max/2400/0*wXv5wPeEmUDMgWYg.png" alt="">
<p>Biraz daha aşağılara indiğimizde, komut çalıştırmak için SHELL32.DLL ‘yi kullandığını gözlemliyorum.</p>
<img src="https://miro.medium.com/max/2400/0*cBQHHocTxp4TjvpL.png" alt="">

### [](#header-3)Remnux

<p>Sonrasında trojeni farkı bir ortamda incelemek için Remnux üzerinden analiz yapmaya devam ediyorum.</p>
<p>Zararlı kod Remnux tarafından pescanner aracı ile incelediğimde aşağıdaki gibi bir çıktı elde ediyoruz.</p>
<img src="https://miro.medium.com/max/2400/0*Ed8GkQLCJkWMEPjD.png" alt="">
<img src="https://miro.medium.com/max/2400/0*8IygsshMms_QXt9X.png" alt="">
<p>Çıktıda şüpheli DLL dosyaları ve bu DLL’lerin kullandığı fonksiyonlara ait bilgiler gösterilmiştir. <b>CreateFileA</b> , <b>CreateFileW</b> fonksiyonları dosya okuma ve yazma işlemleri için , <a style="color:red;">I am red</a> , <b>closesocket</b> fonksiyonları ağ bağlantısı açıp kapatmak için , <b>GetVersionExA</b> işletim sistemi versiyonun öğrenilmesi için , <b>GetCommandLineW</b> komut satırından komut çalıştırmak için, <b>LoadLibraryA</b> kütüphane yükleme işlemi için , <b>TerminateProcess</b> süreç sonlandırmak için kullanılan fonksiyonlardır. Araç bu fonksiyonları şüpheli olarak yorumlamıştır.</p>

#### [](#header-4)Kaynaklar

*   https://www.amazon.com.tr/Someler-%C4%B0%C3%A7in-A%C4%9F-Malware-Analizi/dp/6053446378/ref=asc_df_6053446378/?tag=googleshoptr-21&linkCode=df0&hvadid=344917407350&hvpos=&hvnetw=g&hvrand=2716014781462081402&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1012773&hvtargid=pla-712550236253&psc=1
*   https://kamransaifullah.medium.com/practical-malware-analysis-chapter-1-basic-static-analysis-44c4532c439



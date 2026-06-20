"""
Management command untuk mengisi data awal basis pengetahuan.
Jalankan: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from core.models import Penyakit, Gejala, Rule

PENYAKIT = [
    ("P01", "Jembrana",
     "Penyakit virus (lentivirus) akut yang menyerang sapi Bali dan kerbau, ditandai dengan demam tinggi, "
     "pembesaran kelenjar getah bening, dan dapat menyebabkan kematian dalam 1-2 minggu. "
     "Berbeda dengan lentivirus lain yang kronis, penyakit Jembrana bersifat akut dengan tingkat kematian 20-30%. "
     "(Sumber: ResearchGate, Cambridge University Press)",
     "Isolasi hewan segera. Tidak ada pengobatan spesifik. Berikan antibiotik untuk infeksi sekunder, "
     "cairan elektrolit untuk dehidrasi, dan perawatan suportif. Vaksinasi pencegahan tersedia. "
     "Laporkan ke dinas peternakan."),
    ("P02", "Baliziekte",
     "Bali Ziekte merupakan penyakit hipersensitivitas yang disebabkan oleh racun Lantana camara yang dimakan sapi sehingga mengakibatkan kulit terkelupas dan luka.",
     "Isolasi sapi dari sumber tanaman beracun, pindahkan ke tempat teduh, berikan terapi suportif dan perawatan luka. Konsultasikan dengan dokter hewan untuk penanganan lebih lanjut."),
    ("P03", "Cacingan (Toxocara vitulorum)",
     "Infeksi cacing gelang besar (roundworm) yang menyerang anak sapi usia 1-6 bulan. "
     "Cacing berwarna putih krem hingga 30 cm panjangnya. Penularan melalui susu induk yang terinfeksi. "
     "Dapat menyebabkan diare, penurunan pertumbuhan, obstruksi usus, bahkan kematian pada kasus berat. "
     "(Sumber: University of Saskatchewan, NIH, Merck Veterinary Manual)",
     "Berikan anthelmintik (obat cacing): fenbendazole, albendazole, atau ivermectin sesuai dosis. "
     "Obati induk sapi sebelum melahirkan untuk mencegah penularan. Sanitasi kandang dan rotasi padang rumput. "
     "Perawatan suportif untuk diare dan dehidrasi."),
    ("P04", "Corpus Luteum Persisten",
     "Gangguan reproduksi dimana corpus luteum (CL) tetap aktif di ovarium melebihi waktu normal "
     "sehingga sapi tidak menunjukkan tanda-tanda birahi dan dianggap bunting padahal tidak. "
     "Menyebabkan anovulasi (tidak ada ovulasi) dan meningkatkan jarak beranak (calving interval). "
     "(Sumber: Merck Veterinary Manual, Partners in Reproduction)",
     "Injeksi prostaglandin F2α (PGF2α) untuk melisiskan CL persisten. Dapat diulang jika diperlukan. "
     "Evaluasi dengan ultrasonografi untuk memastikan diagnosis. Periksa kondisi uterus untuk mendeteksi "
     "endometritis yang sering menyertai. Perbaiki manajemen reproduksi dan nutrisi."),
    ("P05", "Surra (Trypanosomiasis)",
     "Penyakit parasit darah (Trypanosoma evansi) yang ditularkan oleh lalat penghisap darah (Tabanids, Stomoxes). "
     "Menyebabkan demam berulang, anemia progresif, penurunan berat badan, dan penurunan produksi. "
     "Dapat berakibat fatal terutama pada kuda dan unta, sedang pada sapi bersifat kronis. "
     "(Sumber: CABI, WOAH, FAO, UK Government)",
     "Berikan obat tripanosida: diminazene aceturate atau isometamidium chloride. "
     "Kontrol vektor dengan insektisida dan perangkap lalat. Pisahkan hewan sakit. "
     "Monitor dengan pemeriksaan darah mikroskopis. Perbaiki nutrisi untuk meningkatkan daya tahan."),
    ("P06", "Bovine Ephemeral Fever (Demam 3 Hari)",
     "Penyakit virus (rhabdovirus) akut yang ditularkan oleh serangga (nyamuk). "
     "Ditandai dengan demam tinggi mendadak, kekakuan otot, pincang, air liur berlebih, dan keengganan bergerak. "
     "Disebut 'demam 3 hari' karena gejala biasanya berlangsung 2-3 hari. Mortalitas rendah (<1%) tapi "
     "menyebabkan penurunan produksi susu drastis dan kerugian ekonomi. "
     "(Sumber: Merck Veterinary Manual, Springer, Australia NSW, NIH)",
     "Tidak ada pengobatan spesifik. Berikan NSAID (anti-inflamasi non-steroid) seperti flunixin meglumine "
     "untuk mengurangi demam dan nyeri. Perawatan suportif: cairan, bantuan berdiri untuk sapi rebah. "
     "Vaksinasi pencegahan tersedia. Kontrol serangga vektor. Pemulihan biasanya spontan dalam 3-7 hari."),
]

GEJALA = [
    ("G01", "Demam (Dengan suhu 38-40 Derajat Celcius)"),
    ("G02", "Pembengkakan hebat kelenjar limfe"),
    ("G03", "Mengeluarkan keringat darah"),
    ("G04", "Diare yang sering bercampur darah"),
    ("G05", "Keluarnya air liur yang berlebih"),
    ("G06", "Penurunan bobot badan"),
    ("G07", "Luka pada selaput lendir mulut"),
    ("G08", "Pucat atau Anemia"),
    ("G09", "Mata berlendir atau berair"),
    ("G10", "Peradangan pada daerah hidung"),
    ("G11", "Gatal-gatal dan ternak sapi tidak tenang"),
    ("G12", "Keropeng pada kulit"),
    ("G13", "Kesakitan pada bagian tubuh tertentu"),
    ("G14", "Diare"),
    ("G15", "Kurus"),
    ("G16", "Tidak nafsu makan"),
    ("G17", "Bulu kusam dan berdiri"),
    ("G18", "Telinga sapi tampak terkulai"),
    ("G19", "Tidak birahi"),
    ("G20", "Peradangan pada dinding rahim"),
    ("G21", "Penumpukan nanah di alat reproduksi"),
    ("G22", "Kematian anak sapi di dalam perut induk"),
    ("G23", "Janin dalam kandungan membusuk dan mengalami proses penguraian dalam rahim"),
    ("G24", "Nafsu makan akan berkurang"),
    ("G25", "Bulu rontok"),
    ("G26", "Bagian bawah dagu dan kaki terlihat kotor"),
    ("G27", "Berputar-putar tanpa arah"),
    ("G28", "Keluar getah radang dari hidung dan mata"),
    ("G29", "Berjalan sempoyongan"),
    ("G30", "Kejang"),
    ("G31", "Demam (Dengan suhu 41 Derajat Celcius)"),
    ("G32", "Kelihatan tubuh gemetar"),
    ("G33", "Ileleran pada hidung dan mata"),
    ("G34", "Kesakitan dan kaku pada otot"),
    ("G35", "Frekuensi nafas dan jantung meningkat"),
]

# (kode_penyakit, kode_gejala, cf_pakar)
RULES = [
    ("P01","G01",0.6), ("P01","G02",0.8), ("P01","G03",0.8), ("P01","G04",0.6), ("P01","G05",0.6), ("P01","G06",0.6), ("P01","G07",0.6),
    ("P02","G01",0.6), ("P02","G08",0.6), ("P02","G09",0.8), ("P02","G10",0.8), ("P02","G11",0.8), ("P02","G12",0.8), ("P02","G13",0.6),
    ("P03","G09",0.8), ("P03","G14",0.8), ("P03","G15",0.8), ("P03","G16",0.8), ("P03","G17",0.8), ("P03","G18",0.8),
    ("P04","G13",0.6), ("P04","G19",0.8), ("P04","G20",0.6), ("P04","G21",0.6), ("P04","G22",0.6), ("P04","G23",0.6),
    ("P05","G01",0.6), ("P05","G24",0.8), ("P05","G25",0.8), ("P05","G26",0.8), ("P05","G27",0.8), ("P05","G28",0.8), ("P05","G29",0.8), ("P05","G30",0.8),
    ("P06","G24",0.8), ("P06","G31",0.8), ("P06","G32",0.8), ("P06","G33",0.8), ("P06","G34",0.8), ("P06","G35",0.6),
]


class Command(BaseCommand):
    help = "Isi data awal penyakit, gejala, dan rule CF."

    def handle(self, *args, **kwargs):
        p_map = {}
        for kode, nama, desk, solusi in PENYAKIT:
            obj, created = Penyakit.objects.get_or_create(kode=kode, defaults={"nama": nama, "deskripsi": desk, "solusi": solusi})
            p_map[kode] = obj
            if created:
                self.stdout.write(f"  + Penyakit: {obj}")

        g_map = {}
        for kode, nama in GEJALA:
            obj, created = Gejala.objects.get_or_create(kode=kode, defaults={"nama": nama})
            g_map[kode] = obj
            if created:
                self.stdout.write(f"  + Gejala: {obj}")

        for kp, kg, cf in RULES:
            _, created = Rule.objects.get_or_create(penyakit=p_map[kp], gejala=g_map[kg], defaults={"cf_pakar": cf})
            if created:
                self.stdout.write(f"  + Rule: {kp}|{kg}|CF={cf}")

        self.stdout.write(self.style.SUCCESS("Seed data selesai!"))

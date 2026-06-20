"""
Management command untuk mengisi data Solusi Penanganan yang komprehensif.
Data disusun berdasarkan literatur veteriner terpercaya dan best practices.

Sumber Referensi:
- MSD Veterinary Manual
- WHO/WOAH (World Organisation for Animal Health)  
- NIH (National Institutes of Health) - PubMed
- FAO (Food and Agriculture Organization)
- University Extension Services (Wisconsin, Minnesota, etc)
- Government Veterinary Guidelines (UK, Australia, USA)

Jalankan: python manage.py seed_solusi
"""
from django.core.management.base import BaseCommand
from core.models import Penyakit, SolusiPenanganan


# Data solusi penanganan untuk semua penyakit
# Format: (kode_penyakit, jenis, judul, deskripsi, prioritas, referensi)
SOLUSI_DATA = [
   
    # ========== P01: JEMBRANA ==========
    ("P01", "pengobatan", "Terapi Suportif dan Antibiotik Sekunder",
     "Tidak ada antiviral spesifik untuk Jembrana Disease Virus. Berikan terapi suportif: (1) Cairan elektrolit IV/SC untuk rehidrasi "
     "(Ringer's Lactate atau NaCl 0.9%) 20-40 ml/kg; (2) Vitamin B complex dan multivitamin injeksi untuk support metabolisme; "
     "(3) Antibiotik broad-spectrum (oxytetracycline 10-20mg/kg atau florfenicol 20mg/kg) untuk cegah infeksi bakterial sekunder; "
     "(4) NSAID untuk demam (flunixin meglumine 1-2mg/kg). Prognosis buruk jika sudah severe - mortalitas 20-30%. Terapi paling efektif pada early stage.",
     1, "ResearchGate - Immunodiagnosis in Jembrana Disease; Cambridge - Transmission of Jembrana Disease"),
    
    ("P01", "manajemen", "Isolasi dan Kontrol Vektor",
     "Isolasi segera sapi sakit minimum 500 meter dari herd sehat. Virus ditransmit melalui darah - hindari sharing needles/equipment antar sapi. "
     "Vektor mekanis: lalat Tabanid dan Stomoxys - control dengan insektisida spray (permethrin, cypermethrin) dan fly traps. "
     "Cuci dan sterilisasi semua equipment yang kontak dengan darah (alat suntik, scalpel, ear tag applicator). Karantina hewan baru 30 hari dengan tes darah. "
     "Disease endemik di Bali - avoid transporting Bali cattle ke area naive. Report ke otoritas - disease adalah reportable di Indonesia.",
     2, "CABI Datasheet - Jembrana Disease; WOAH Listed Disease"),
    
    ("P01", "vaksinasi", "Vaksinasi Preventif (Indonesia)",
     "Vaksin Jembrana disease tersedia di Indonesia (inactivated vaccine). Vaksinasi sapi umur >3 bulan di area endemik (Bali, Nusa Tenggara). "
     "Schedule: vaksinasi awal 2 dosis dengan interval 3-4 minggu, booster setiap 6-12 bulan. Immunity berkembang 2-3 minggu pascavaksinasi kedua. "
     "Proteksi: reduce clinical severity dan mortalitas, tidak 100% prevent infection. Kombinasi vaksinasi + vector control + biosecurity untuk "
     "kontrol optimal. Vaksinasi wajib untuk sapi yang akan dipindahkan dari area endemik.",
     3, "Bali Veterinary Center; Indonesia Disease Control Program"),
    
    ("P01", "sanitasi", "Desinfeksi dan Pencegahan Transmisi Darah",
     "Virus Jembrana sensitif terhadap desinfektan standar: sodium hypochlorite 1%, iodine compounds, phenolic disinfectants. "
     "Sterilisasi alat medis dengan autoclave (121°C, 15 psi, 15 menit) atau disinfeksi kimia (glutaraldehyde 2%). "
     "Disposable needles dan syringes - JANGAN reuse. Jika harus reuse: sterilisasi proper antara penggunaan. "
     "Hindari tindakan yang involve darah (castration, dehorning, ear tagging) selama outbreak. Burn atau bury dalam bangkai dengan kapur. "
     "Virus dapat survive dalam darah pada needle sampai 24 jam.",
     4, "Veterinary Protocols Indonesia; CABI Compendium"),
    
    # ========== P02: SEPTIKEMIA HEMORAGIK (BALIZIEKTE/HS) ==========
    ("P02", "pengobatan", "Eliminasi Toksin dan Terapi Suportif Intensif",
     "Tidak ada antidotum spesifik untuk keracunan Lantana camara. Pengobatan utama adalah segera menghentikan akses terhadap tanaman penyebab dan memberikan terapi suportif. "
     "Terapi cairan IV untuk mengatasi dehidrasi dan mendukung fungsi hati. Berikan hepatoprotektor seperti silymarin, vitamin B kompleks, vitamin E dan selenium sesuai rekomendasi dokter hewan. "
     "NSAID dapat diberikan untuk mengurangi inflamasi dan nyeri. Pada kasus pruritus berat dapat dipertimbangkan antihistamin. "
     "Hewan dengan anoreksia memerlukan dukungan nutrisi dan pakan berkualitas tinggi. Prognosis baik pada kasus ringan yang ditangani dini, "
     "namun menjadi buruk apabila telah terjadi kerusakan hati berat, ikterus, atau nekrosis kulit luas akibat fotosensitisasi.",
     1, "Kasus Keracunan Lantana camara pada Sapi Bali; Literatur Toksikologi Veteriner"),
        
    ("P02", "manajemen", "Isolasi dari Sinar Matahari dan Monitoring Hati",
     "Segera pindahkan sapi ke kandang teduh atau area beratap untuk mencegah fotosensitisasi lanjutan. "
     "Batasi paparan sinar matahari terutama pukul 09.00-16.00. Monitor nafsu makan, suhu tubuh, warna mukosa, kondisi kulit, dan fungsi hati secara berkala. "
     "Pisahkan hewan yang menunjukkan gejala klinis untuk memudahkan observasi dan perawatan. "
     "Kasus berat dapat memerlukan pemantauan enzim hati (AST, ALT, GGT) dan status hidrasi. "
     "Pencatatan lokasi padang penggembalaan penting untuk identifikasi sumber keracunan dan pencegahan kasus berulang.",
     2, "Balische Ziekte Reports; Pedoman Manajemen Penyakit Toksik Ruminansia"),
        
    ("P02", "pencegahan", "Pengendalian Tanaman Lantana camara",
     "Pencegahan paling efektif adalah menghilangkan atau membatasi akses ternak terhadap tanaman Lantana camara (kancing landa/lempuyak). "
     "Lakukan inspeksi rutin padang penggembalaan terutama pada musim kemarau saat hijauan pakan terbatas. "
     "Pastikan ketersediaan hijauan dan pakan yang cukup agar ternak tidak mengonsumsi tanaman beracun. "
     "Edukasi peternak mengenai identifikasi tanaman Lantana camara dan gejala awal Baliziekte. "
     "Sapi yang baru dipindahkan ke lokasi penggembalaan baru harus dipantau ketat selama 1-2 minggu pertama.",
     3, "Literatur Keracunan Lantana pada Ruminansia; JITRO Baliziekte"),
        
    ("P02", "sanitasi", "Manajemen Padang Penggembalaan",
     "Lakukan eradikasi mekanis atau kimiawi terhadap tanaman Lantana camara di area penggembalaan. "
     "Rumput dan semak yang telah dipotong harus dibuang dengan aman karena daun yang layu masih dapat bersifat toksik. "
     "Rotasi padang penggembalaan membantu mengurangi risiko konsumsi tanaman beracun. "
     "Pastikan ketersediaan air bersih dan pakan berkualitas baik. "
     "Area dengan kepadatan tinggi tanaman Lantana sebaiknya tidak digunakan untuk penggembalaan sapi sampai dilakukan pembersihan menyeluruh.",
     4, "Toksikologi Veteriner Tanaman Beracun; Kasus Keracunan Lantana camara pada Sapi"),

    # ========== P03: CACINGAN (TOXOCARA VITULORUM) ==========
    ("P03", "pengobatan", "Anthelmintik Broad-Spectrum",
     "Obat cacing pilihan untuk Toxocara vitulorum: (1) Fenbendazole 10mg/kg PO single dose atau 5mg/kg PO selama 3 hari berturut-turut; "
     "(2) Albendazole 10mg/kg PO single dose (JANGAN untuk sapi bunting trimester pertama); (3) Ivermectin 0.2mg/kg SC/PO; "
     "(4) Levamisole 7.5mg/kg SC/PO; (5) Pyrantel pamoate 10mg/kg PO. Ulangi treatment setelah 2-3 minggu untuk kill larva yang baru mature. "
     "Terapi suportif untuk anak sapi severe: cairan SC/IV untuk dehidrasi, vitamin B complex, probiotik untuk restore gut flora. "
     "Monitor feses 7-14 hari post-treatment untuk assess efficacy (fecal egg count).",
     1, "University of Saskatchewan - Toxocara vitulorum; NIH PMC Case Study; MSD Veterinary Manual"),
    
    ("P03", "pencegahan", "Deworm Induk Pra-Partus",
     "Strategi pencegahan utama: deworm sapi induk bunting 2-4 minggu SEBELUM expected calving date. Ini mengurangi transmisi transmammary larvae ke calf. "
     "Anthelmintic untuk sapi bunting: fenbendazole (safe), ivermectin (safe trimester 2-3), levamisole (avoid trimester 1). "
     "Deworm calves pada umur 2-3 minggu (sebelum patent period - prepatent deworming), ulangi umur 6-8 minggu dan 12-16 minggu. "
     "High-risk calves: dari induk dengan riwayat infeksi berat atau area endemik tinggi. Rotational deworming schedule berbasis fecal egg count monitoring.",
     2, "The Beef Site - Toxocara Vitulorum Report; Wormboss Australia"),
    
    ("P03", "manajemen", "Sanitasi Kandang dan Rotasi Padang",
     "Hygiene management: (1) Clean bedding daily untuk remove fecal contamination; (2) Separate young calves dari adult cattle; "
     "(3) Colostrum management: pasteurisasi kolostrum (60°C selama 60 menit) untuk kill larvae; (4) Rotational grazing: pindahkan calves ke clean pasture "
     "setiap 2-4 minggu (larva tidak survive >2 minggu di pasture kering). Hindari overcrowding - increase parasite load. "
     "Fecal egg count monitoring: sample pooled feces setiap 3-6 bulan untuk assess parasite burden dan efficacy deworming program.",
     3, "ResearchGate - Toxocara vitulorum in cattle; Parasitology Extensions"),
    
    ("P03", "nutrisi", "Nutrisi Optimal untuk Resistance",
     "Nutritional support untuk meningkatkan resistance: (1) Protein adequat (CP 14-16% untuk growing calves) - mendukung immune function; "
     "(2) Trace minerals: zinc (40-60ppm), copper (10-15ppm), selenium (0.3ppm) - esensial untuk immunity dan tissue repair; "
     "(3) Vitamin A (2000-4000 IU/kg diet) untuk intestinal mucosa health; (4) Energy adequat (avoid underfeeding) - malnutrisi meningkatkan susceptibility. "
     "Free-choice mineral supplement dengan trace minerals. Monitor body condition score - target BCS 5-6 (skala 1-9) untuk optimal resistance terhadap parasit.",
     4, "NRC Nutrient Requirements; Journal of Veterinary Parasitology"),
    
    # ========== P04: CORPUS LUTEUM PERSISTEN ==========
    ("P04", "pengobatan", "Injeksi Prostaglandin F2α (PGF2α)",
     "Treatment pilihan: Prostaglandin F2α (PGF2α) injeksi untuk luteolysis (hancurkan CL persisten). Dosis: dinoprost tromethamine 25mg IM atau "
     "cloprostenol 500µg IM. CL akan regress dalam 2-5 hari, diikuti estrus dalam 2-5 hari pascainjeksi. Jika tidak estrus setelah 7-10 hari: "
     "ulangi PGF2α (kemungkinan ada CL baru atau cyst). Jangan berikan PGF2α pada sapi bunting (menyebabkan aborsi). "
     "Kombinasi terapi: GnRH (day 0) + PGF2α (day 7) + GnRH (day 9) untuk Ovsynch protocol jika perlu breeding scheduled.",
     1, "MSD Veterinary Manual - Luteal Cystic Ovary; NIH - Effects of GnRH or PGF2α"),
    
    ("P04", "manajemen", "Pemeriksaan Ultrasonografi dan Monitoring",
     "Diagnosis akurat dengan transrectal ultrasonography (TRUS): visualisasi CL persisten (corpus luteum >20mm yang bertahan >18 hari tanpa estrus). "
     "Differensiasi dari pregnancy (presence of embryo/fetus) dan cystic structures. Monitoring herd: check all cows tidak kawin setelah 60 hari postpartum. "
     "Body condition score monitoring: BCS <2.5 atau >3.5 meningkatkan risk persistent CL. Target BCS 3.0-3.25 at calving, 2.5-3.0 early lactation. "
     "Breeding records accurate: heat detection aids (tail paint, pedometers, activity monitors) untuk identify anestrus cows.",
     2, "Partners in Reproduction - Corpus Luteum Persistent; NADIS UK"),
    
    ("P04", "pencegahan", "Pencegahan Endometritis dan Infeksi Uterus",
     "Persistent CL sering berkaitan dengan endometritis (uterine infection). Pencegahan: (1) Clean calving environment; "
     "(2) Proper obstetric hygiene - desinfeksi alat dan tangan; (3) Avoid unnecessary uterine manipulation; (4) Early treatment metritis/endometritis "
     "(PGF2α atau intrauterine antibiotics); (5) Adequate nutrition peripartum untuk cegah immune suppression; (6) Vitamin E (1000 IU/day) dan "
     "selenium (0.3ppm diet) untuk uterine health. Postpartum check 30-40 hari untuk detect endometritis dan reproductive abnormalities dini.",
     3, "MSD Animal Health Ireland - Uterine Infection; Reproduction Extensions"),
    
    ("P04", "nutrisi", "Manajemen Nutrisi dan Body Condition",
     "Nutritional management untuk optimal reproduction: (1) Energy balance positive atau minimal 0 pada breeding period; "
     "(2) Avoid excessive body condition loss postpartum (target <1 BCS loss); (3) Transition cow management: DCAD diet 21 hari prepartum "
     "(prevent milk fever), adequate calcium dan phosphorus; (4) Protein 16-18% CP early lactation; (5) Beta-carotene supplementation "
     "(300-600mg/day) untuk corpus luteum function dan fertility. Monitor milk production, body condition, dan metabolic indicators (BHB, NEFA) "
     "untuk assess energy balance. Consult nutritionist untuk optimize reproduction-focused feeding program.",
     4, "Dairy Cattle Fertility Management; NRC Nutrient Requirements of Dairy Cattle"),

    # ========== P05: SURRA (TRYPANOSOMIASIS) ==========
    ("P05", "pengobatan", "Obat Tripanosida Spesifik",
     "Trypanocidal drugs pilihan: (1) Diminazene aceturate (Berenil) 3.5-7mg/kg IM deep injection single dose - drug of choice untuk Trypanosoma evansi. "
     "Efektif untuk infection akut dan kronis. Side effects minimal jika dosis tepat; (2) Isometamidium chloride (Trypamidium) 0.5-1mg/kg IM - "
     "efek terapeutik DAN profilaktik (proteksi 2-4 bulan). Gunakan untuk treatment dan prevention di endemic areas; "
     "(3) Suramin 10mg/kg IV (slow) - jarang digunakan karena toxicity lebih tinggi. Treatment harus diulang jika relapse (recurrence parasitemia). "
     "Monitor blood smear 7, 14, 21 hari post-treatment untuk assess cure. Terapi suportif: iron supplementation untuk anemia, vitamin B complex.",
     1, "CABI - Trypanosoma evansi; WOAH Chapter 8.23; FAO Field Guide"),
    
    ("P05", "manajemen", "Kontrol Vektor Lalat Penghisap Darah",
     "Vector control strategies: (1) Insekticide treatment: pour-on pyrethroid (deltamethrin, cypermethrin) setiap 2-4 minggu atau ear tags insecticide; "
     "(2) Fly traps: sticky traps, odor-baited traps untuk Tabanid flies dan Stomoxys; (3) Residual spraying: kandang walls dan resting areas dengan "
     "residual insecticide; (4) Environmental management: drain standing water (breeding site Tabanus), remove manure regularly, vegetation control "
     "around farm. Timing: vector control intensif during high fly season (panas/lembab). Integrated pest management lebih efektif dari single approach.",
     2, "UK Government - Surra Disease; ResearchGate - Trypanosomosis in Livestock"),
    
    ("P05", "pencegahan", "Chemoprophylaxis dan Screening",
     "Preventive chemotherapy di endemic areas: Isometamidium chloride 0.5mg/kg IM memberikan proteksi 2-6 bulan (tergantung challenge). "
     "Strategic prophylaxis: inject sebelum high-risk period (musim fly peak, transhumance, mixing herds). Quarantine dan test hewan baru: "
     "blood smear examination (Giemsa stain), serologi (CATT, ELISA) sebelum masuk herd. Isolasi 30-60 hari dengan monitoring clinical signs. "
     "Avoid sharing needles/instruments (mechanical transmission). Sterilisasi equipment bedah proper. Di Latin America: vampire bat control juga penting.",
     3, "WOAH Standards; CABI Compendium; FAO Guidelines"),
    
    ("P05", "nutrisi", "Nutritional Support untuk Recovery",
     "Nutritional support untuk sapi terinfeksi: (1) High-quality protein 14-16% CP untuk restore muscle mass yang loss dari cachexia; "
     "(2) Iron supplementation: iron dextran injection 10-20mg/kg IM atau oral ferrous sulfate untuk combat anemia (Hb <8g/dl); "
     "(3) Vitamin B12 (cyanocobalamin) 1000-5000µg IM weekly untuk support erythropoiesis; (4) Folic acid 5-10mg/day untuk blood cell production; "
     "(5) Energy adequat: high-quality forage + grain supplement untuk weight recovery. Monitor PCV (packed cell volume) weekly - target >25% untuk recovery. "
     "Avoid stress selama recovery period. Good nutrition meningkatkan treatment response dan reduce relapse rate.",
     4, "Journal of Tropical Animal Health; Veterinary Parasitology Reviews"),
    
    # ========== P06: BOVINE EPHEMERAL FEVER (DEMAM 3 HARI) ==========
    ("P06", "pengobatan", "NSAID dan Terapi Suportif",
     "Tidak ada antiviral spesifik - treatment adalah symptomatic dan supportive. (1) NSAID untuk demam dan nyeri: Flunixin meglumine 1-2.2mg/kg IV/IM "
     "setiap 12-24 jam atau Ketoprofen 3mg/kg IV/IM atau Meloxicam 0.5mg/kg SC - reduce fever, inflammation, muscle stiffness; "
     "(2) Cairan therapy: Ringer's Lactate atau NaCl 0.9% 20-40ml/kg IV untuk dehydration dan support circulation; "
     "(3) Calcium borogluconate IV jika ada hypocalcemia signs (muscle tremors, recumbency); (4) Vitamin B complex injection untuk support metabolism. "
     "Nursing care: soft bedding untuk recumbent cows, flip/reposition setiap 3-4 jam (prevent pressure sores), sling support jika perlu. "
     "Recovery spontan 3-7 hari pada majority cases. Mortalitas <1% kecuali komplikasi (pneumonia, mastitis sekunder).",
     1, "MSD Veterinary Manual - BEF; Springer - Epidemiology BEF; Australia NSW Department"),
    
    ("P06", "manajemen", "Supportive Care untuk Sapi Rebah",
     "Management recumbent cows (down cows): (1) Thick bedding (straw, sand, mattress) untuk prevent pressure necrosis; "
     "(2) Reposition cow setiap 3-4 jam untuk prevent muscle dan nerve damage; (3) Hip lifters atau slings untuk assist standing; "
     "(4) Massage muscles untuk prevent atrophy dan improve circulation; (5) Encourage standing attempts 4-6x per hari dengan assistance; "
     "(6) Hand-fed high-quality feed dan water jika tidak mau eat/drink; (7) Milk out secara manual atau machine untuk prevent mastitis. "
     "Monitor for complications: pneumonia (dari recumbency), pressure sores, nerve paralysis, mastitis. "
     "Hindari force standing terlalu awal - bisa cause secondary injuries. Patience - majority recover dalam 5-7 hari dengan good nursing care.",
     2, "CSIRO Microbiology Australia; NIH - BEF in Asia; ResearchGate - BEF Australia"),
    
    ("P06", "vaksinasi", "Vaksinasi Preventif Tahunan",
     "Inactivated BEF vaccine available di endemic countries (Australia, Asia). Vaksinasi sapi >6 bulan umur. Schedule: (1) Primary course: 2 doses "
     "dengan interval 4-6 minggu; (2) Booster: annual booster 2-4 minggu SEBELUM expected BEF season (vector activity peak - panas/musim hujan). "
     "Immunity berkembang 2-3 minggu pascavaksinasi kedua. Duration of immunity: 12 bulan. Vaksinasi tidak prevent infection 100% tetapi significantly "
     "reduce clinical severity, duration of disease, dan milk production loss. High-value animals (dairy high producers, bulls) prioritas vaksinasi. "
     "Vaksinasi tidak efektif jika diberikan SAAT outbreak sudah terjadi (perlu waktu immunity development).",
     3, "Queensland Australia - BEF; Journal Vaccine - BEF Vaccines; Veterinary Record"),
    
    ("P06", "sanitasi", "Kontrol Vektor Nyamuk dan Culicoides",
     "Vector control untuk prevent BEF transmission: (1) Insecticide application: pour-on pyrethroid atau spray premises dengan residual insecticide "
     "(permethrin, deltamethrin) terutama evening/night (vector activity peak); (2) Repellents: insect repellent pada cattle selama high-risk periods; "
     "(3) Environmental management: eliminate standing water (breeding sites nyamuk), drain ditches, remove vegetation near housing; "
     "(4) Housing management: screen housing jika feasible, fans untuk air circulation (reduce vector contact); (5) Timing: intensify vector control "
     "2-4 minggu before expected disease season. BEF is vector-borne (mosquitoes, Culicoides) - tidak direct cattle-to-cattle transmission. "
     "Control vectors = control disease spread. Integrated approach: vaksinasi + vector control untuk optimal protection.",
     4, "Elsevier - Textbook Diseases of Cattle; Veterinary Entomology Reviews"),
]


class Command(BaseCommand):
    help = "Isi data Solusi Penanganan komprehensif untuk semua penyakit dari sumber terpercaya."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("=" * 80))
        self.stdout.write(self.style.SUCCESS("MENGISI DATA SOLUSI PENANGANAN KOMPREHENSIF"))
        self.stdout.write(self.style.SUCCESS("=" * 80))
        
        # Mapping kode penyakit ke objek
        penyakit_map = {}
        for penyakit in Penyakit.objects.all():
            penyakit_map[penyakit.kode] = penyakit
        
        created_count = 0
        updated_count = 0
        
        for kode_penyakit, jenis, judul, deskripsi, prioritas, referensi in SOLUSI_DATA:
            if kode_penyakit not in penyakit_map:
                self.stdout.write(self.style.WARNING(f"  ⚠️  Penyakit {kode_penyakit} tidak ditemukan, skip."))
                continue
            
            penyakit_obj = penyakit_map[kode_penyakit]
            
            # Cek apakah solusi sudah ada (berdasarkan penyakit + jenis + judul)
            obj, created = SolusiPenanganan.objects.get_or_create(
                penyakit=penyakit_obj,
                jenis=jenis,
                judul=judul,
                defaults={
                    'deskripsi': deskripsi,
                    'prioritas': prioritas,
                    'referensi': referensi,
                    'aktif': True,
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"  ✅ {penyakit_obj.kode} - {jenis}: {judul[:50]}..."))
            else:
                # Update jika sudah ada
                obj.deskripsi = deskripsi
                obj.prioritas = prioritas
                obj.referensi = referensi
                obj.save()
                updated_count += 1
                self.stdout.write(self.style.WARNING(f"  🔄 {penyakit_obj.kode} - {jenis}: {judul[:50]}... (updated)"))
        
        # Statistik
        self.stdout.write("\n" + "=" * 80)
        self.stdout.write(self.style.SUCCESS("📊 STATISTIK:"))
        self.stdout.write(f"  • Solusi baru dibuat: {created_count}")
        self.stdout.write(f"  • Solusi diupdate: {updated_count}")
        self.stdout.write(f"  • Total solusi di database: {SolusiPenanganan.objects.count()}")
        self.stdout.write("=" * 80)
        
        # Summary per penyakit
        self.stdout.write("\n📋 RINGKASAN PER PENYAKIT:")
        for penyakit in Penyakit.objects.all().order_by('kode'):
            jumlah = penyakit.solusi_penanganan.filter(aktif=True).count()
            self.stdout.write(f"  {penyakit.kode} - {penyakit.nama}: {jumlah} solusi aktif")
        
        self.stdout.write("\n" + "=" * 80)
        self.stdout.write(self.style.SUCCESS("🎉 SELESAI! Data solusi penanganan berhasil diisi."))
        self.stdout.write("\n📚 SUMBER REFERENSI:")
        self.stdout.write("  • MSD Veterinary Manual")
        self.stdout.write("  • WHO/WOAH - World Organisation for Animal Health")
        self.stdout.write("  • NIH/PubMed - National Institutes of Health")
        self.stdout.write("  • University Extensions (Wisconsin, Minnesota, etc)")
        self.stdout.write("  • FAO - Food and Agriculture Organization")
        self.stdout.write("  • Government Veterinary Services (UK, Australia, USA)")
        self.stdout.write("  • Peer-reviewed Veterinary Journals")
        self.stdout.write("\n")

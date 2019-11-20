import os
import os.path as path




def checkPath(filePath):
    extensionDictionary = [ #Created new line for readability
    '.$$$', '.$$A', '.$$F', '.$$S', '.$D$', '.$DB', '.$ED', '.$VM', '._DD', '._DM', '.---',
    '.075', '.085', '.091', '.096', '.0B', '.1ST', '.2GR', '.386', '.3DT', '.3G2', '.3GP',
    '.3GR', '.4SW', '.A', '.A3W', '.ABK', '.ABR', '.ACE', '.ACR', '.ACT', '.AD', '.ADF',
    '.ADM', '.ADP', '.ADR', '.AI', '.AIF', '.AIR', '.ANI', '.ANS', '.APK', '.ARC', '.ARJ',
    '.AS', '.ASC', '.ADF', '.ASL', '.ASP', '.ATO', '.ATY', '.AU', '.AVI', '.AXX', '.B3D',
    '.B64', '.BAK', '.BAR', '.BAS', '.BAT', '.BBS', '.BFC', '.BG', '.BIN', '.BK2', '.BK3',
    '.BK4', '.BK5', '.BK6', '.BK7', '.BK8', '.BK9', '.BMP', '.BNK', '.BPS', '.BPT', '.BR5',
    '.BRK', '.BTOA', '.BUP', '.BV1', '.BV2', '.BV3', '.BV4', '.BV5', '.BV6', '.BV7', '.BV8',
    '.BV9', '.BWP', '.BZ', '.BZ2', '.C', '.CAB', '.CAL', '.CAM', '.CAP', '.CAS', '.CBL',
    '.CBT', '.CDA', '.CDR', '.CDT', '.CFB', '.CFG', '.CFL', '.CFM', '.CGM', '.CHK', '.CL',
    '.CL3', '.CL4', '.CLA', '.CLG', '.CLK', '.CLL', '.CLO', '.CLP', '.CLR', '.CLS', '.CMD',
    '.CMV', '.CNT', '.CPL', '.CNE', '.CNF', '.CNV', '.COB', '.COD', '.COM', '.CPE', '.CPI',
    '.CPP', '.CPT', '.CR2', '.CRD', '.CRT', '.CRW', '.CSI', '.CSV', '.CUE', '.CUR', '.CV5',
    '.CVI', '.CVS', '.CVX', '.CXX', '.D', '.DAA', '.DAF', '.DAT', '.DB', '.DB2', '.DBC',
    '.DBF', '.DBK', '.DBM', '.DBO', '.DBQ', '.DBT', '.DBV', '.DBW', '.DBX', '.DCM', '.DCR',
    '.DCX', '.DDF', '.DDS', '.DEB', '.DEV', '.DIB', '.DIF', '.DJVU', '.DLL', '.DM', '.DMD',
    '.DMF', '.DMG', '.DMO', '.DMP', '.DMS', '.DNE', '.DNG', '.DOC', '.DOCM', '.DOCX', '.DOS',
    '.DOT', '.DOTM', '.DOTX', '.DRV', '.DRW', '.DST', '.DT_', '.DTA', '.DTD', '.DTF', '.DTM',
    '.DTP', '.DUN', '.DX', '.DXB', '.DXF', '.DXN', '.DXR', '.DYN', '.DWF', '.DWG', '.EAP',
    '.ECO', '.EEB', '.EEF', '.EFT', '.EGA', '.ELG', '.EMF', '.EMI', '.EML', '.EMS', '.EMU',
    '.ENC', '.END', '.ENG', '.ENV', '.EPG', '.EPS', '.EPUB', '.EQN', '.ERD', '.ERM', '.ERR',
    '.ESD', '.ESH', '.ET', '.EVT', '.EX3', '.EXC', '.EXD', '.EXE', '.EXO', '.EXT', '.F4V',
    '.FCP', '.FDF', '.FES', '.FF', '.FFA', '.FFF', '.FFL', '.FFO', '.FFT', '.FFX', '.FITS',
    '.FLV', '.FND', '.FON', '.FPB', '.FPR', '.FPX', '.FQY', '.FR3', '.FRC', '.FRF', '.FRG',
    '.FRK', '.FRM', '.FRO', '.FRP', '.FRS', '.FRT', '.FRX', '.FRZ', '.FSC', '.FSH', '.G3',
    '.GHO', '.GIF', '.GR2', '.GR3', '.GRA', '.GRB', '.GRF', '.GRP', '.GZ', '.HBK', '.HDL',
    '.HDR', '.HDX', '.HEIC', '.HEIF', '.HEX', '.HFI', '.HGL', '.HH', '.HHH', '.HHP', '.HPGL',
    '.HQX', '.HSQ', '.HSS', '.HST', '.HTA', '.HTM', '.HTML', '.HTT', '.ICA', '.ICB', '.ICC',
    '.ICE', '.ICL', '.ICM', '.ICN', '.ICO', '.ICS', '.ID', '.IDB', '.IDD', '.IDE', '.IDF',
    '.IDQ', '.IDX', '.IFF', '.IFO', '.IGS', '.IMA', '.IMG', '.INF', '.INI', '.INS', '.IPA',
    '.IPD', '.IPF', '.ISO', '.IW44', '.IWA', '.J2K', '.JAR', '.JAS', '.JEF', '.JNG', '.JP2',
    '.JPC', '.JPEG', '.JPG', '.JPM', '.JS', '.JSB', '.JSD', '.JSE', '.JSH', '.JSL', '.JSM',
    '.JSP', '.JSS', '.JT', '.JTF', '.JTK', '.JTP', '.JW', '.JWL', '.JZZ', '.KAR', '.KBC',
    '.KDC', '.KDP', '.KEY', '.KFX', '.KYE', '.LBM', '.LDF', '.LGC', '.LGO', '.LHA', '.LIB',
    '.LOG', '.LNK', '.LWF', '.LWP', '.LZH', '.M3U', '.M3U8', '.M4A', '.M4V', '.MAC', '.MBX',
    '.MCD', '.MD', '.MDA', '.MDB', '.MDE', '.MDF', '.MDL', '.MDM', '.MDN', '.MDP', '.MDT',
    '.MDW', '.MDX', '.MDZ', '.MEB', '.MED', '.MEM', '.MHT', '.MID', '.MIM', '.MIX', '.MK3D',
    '.MKA', '.MKS', '.MKV', '.MME', '.MNG', '.MOD', '.MOV', '.MP1', '.MP2', '.MP3', '.MPG',
    '.MPK', '.MPL', '.MPP', '.MRW', '.MSC', '.MSI', '.MSN', '.MSP', '.MTF', '.MTH', '.MTM',
    '.MTV', '.MTW', '.MU', '.MUL', '.MUP', '.MUS', '.MVB', '.MVE', '.MVF', '.MWP', '.MXD',
    '.MXT', '.MYD', '.N64', '.NA2', '.NAB', '.NAP', '.NDF', '.NDS', '.NDX', '.NEF', '.NES',
    '.NETA', '.NFO', '.NIL', '.NGF', '.NGG', '.NHF', '.NIL', '.NLB', '.NLD', '.NLM', '.NMI',
    '.NOL', '.NON', '.NOW', '.NRA', '.NRB', '.NRG', '.NS2', '.NS5', '.NS0', '.NT', '.NUM',
    '.NZB', '.OBJ', '.OCA', '.OCX', '.ODT', '.OGG', '.OGM', '.OLB', '.OLD', '.OLE', '.OLI',
    '.ORF', '.ORI', '.OTL', '.OVA', '.PAB', '.PAK', '.PAT', '.PB', '.PBD', '.PBF', '.PBK',
    '.PBL', '.PBM', '.PBR', '.PBI', '.PBM', '.PBO', '.PBT', '.PCD', '.PCT', '.PCX', '.PDA',
    '.PDB', '.PDD', '.PDF', '.PDL', '.PDS', '.PDV', '.PDW', '.PEF', '.PEM', '.PF', '.PGM',
    '.PIC', '.PICT', '.PIF', '.PJF', '.PKG', '.PL', '.PL3', '.PLB', '.PLC', '.PLD', '.PLG',
    '.PLI', '.PLL', '.PLM', '.PLN', '.PLR', '.PLS', '.PLT', '.PLY', '.PNG', '.POT', '.PP',
    '.PP4', '.PP5', '.PPA', '.PPB', '.PPD', '.PPF', '.PPI', '.PPL', '.PPM', '.PPO', '.PPP',
    '.PPS', '.PPT', '.PPTX', '.PPX', '.PPZ', '.PS2', '.PSD', '.PSP', '.PST', '.PWA', '.PWD',
    '.PWF', '.PWL', '.PWP', '.PWZ', '.PX', '.PXL', '.PY', '.PYC', '.PYD', '.PYW', '.PZ2',
    '.PZ3', '.PZA', '.PZD', '.PZL', '.PZO', '.PZP', '.PZS', '.PZT', '.PZX', '.QIC', '.QT',
    '.QTIF', '.QXD', '.QXL', '.QXT', '.R00', '.RA', '.RAF', '.RAM', '.RAR', '.RAS', '.RC',
    '.RD1', '.RD3', '.RD4', '.RD5', '.RDB', '.RDF', '.RDL', '.RDX', '.REC', '.RGB', '.RLE',
    '.RMI', '.RPB', '.RPD', '.RPM', '.RPT', '.RTF', '.RWZ', '.SAV', '.SC2', '.SCP', '.SCR',
    '.SCT', '.SD', '.SD2', '.SDA', '.SDC', '.SDD', '.SDF', '.SDK', '.SDL', '.SDN', '.SDR',
    '.SDS', '.SDT', '.SDV', '.SDW', '.SDX', '.SE', '.SEA', '.SFF', '.SFV', '.SFW', '.SGI',
    '.SH', '.SH3', '.SHB', '.SHG', '.SHK', '.SHM', '.SHP', '.SHR', '.SHS', '.SHTML', '.SHW',
    '.SID', '.SIT', '.SITX', '.SLK', '.SMIL', '.SND', '.SNG', '.SNM', '.SNO', '.SNP', '.SPD',
    '.SRF', '.SRT', '.STP', '.SUM', '.SUN', '.SVG', '.SWF', '.SWP', '.SXC', '.SYS', '.TAR',
    '.TAR.GZ', '.TBZ', '.TBZ', '.TBZ2', '.TDF', '.TGA', '.TGZ', '.TIF', '.TLB', '.TLD',
    '.TLE', '.TLP', '.TLT', '.TLX', '.TMP', '.TOPC', '.TORRENT', '.TPC', '.TRM', '.TRS',
    '.TXT', '.UNI', '.UNK', '.UNX', '.URL', '.UU', '.UUE', '.VB', '.VBA', '.VBD', '.VBE',
    '.VBG', '.VBK', '.VBL', '.VBP', '.VBR', '.VBS', '.VBW', '.VBX', '.VBZ', '.VC', '.VCD',
    '.VCE', '.VCF', '.VCS', '.VCT', '.VCW', '.VCX', '.VDA', '.VDD', '.VDO', '.VDX', '.VLS',
    '.VM', '.VMM', '.VMF', '.VMH', '.VOB', '.VS2', '.VSD', '.VSDM', '.VSL', '.VSS', '.VSSM',
    '.VSSX', '.VST', '.VSW', '.VXD', '.WAB', '.WAD', '.WAL', '.WAV', '.WB1', '.WB2', '.WBF',
    '.WBK', '.WBMP', '.WBT', '.WCD', '.WCM', '.WCP', '.WDB', '.WEB', '.WEBM', '.WFM', '.WFN',
    '.WFX', '.WG1', '.WG2', '.WID', '.WIN', '.WIZ', '.WK1', '.WK3', '.WK4', '.WKS', '.WKG',
    '.WMA', '.WMF', '.WMV', '.WMZ', '.WPD', '.WPG', '.WPM', '.WPS', '.WRI', '.WWK', '.WSC',
    '.WSF', '.X3F', '.XAP', '.XBM', '.XIF', '.XLB', '.XLR', '.XLS', '.XLSB', '.XLSM', '.XLSX',
    '.XM', '.XML', '.XNK', '.XOT', '.XPI', '.XPM', '.XPS', '.XQT', '.XRF', '.XR1', '.XSL',
    '.XSM', '.XT', '.XTB', '.XWD', '.XWF', '.XXE', '.XY', '.XY3', '.XY4', '.XYP', '.XYW', '.Y',
    '.Y01', '.Y02', '.Y03', '.Y04', '.Y05', '.Y06', '.Y07', '.Y08', '.Y09', '.YAML', '.YUV',
    '.YZ', '.Z', '.ZOO', '.ZIP']

    for n in range(828):
        if extensionDictionary[n].lower() in filePath:
            try:
                path.exists(filePath)
                return filePath
            except:
                TypeError

    for n in range(828):
        modFilePath = filePath + extensionDictionary[n].lower()
        try:
            if path.exists(modFilePath) == True:
                return modFilePath
        except:
            TypeError
        
# revision 30741
# category Package
# catalog-ctan /fonts/ebgaramond
# catalog-date 2013-05-22 20:40:58 +0200
# catalog-license ofl
# catalog-version 0.15 (2013-05-22)
Name:		texlive-ebgaramond
Version:	0.15
Release:	4
Summary:	LaTeX support for EBGaramond fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ebgaramond
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebgaramond.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebgaramond.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
EB Garamond is a revival by Georg Duffner of the 16th century
fonts designed by Claude Garamond. The LaTeX support package
works for (pdf)LaTeX, xeLaTeX and luaLaTeX users; configuration
files for use with microtype are provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_2cg6vv.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_2s43qf.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_3aytur.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_4enc56.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_4o5twj.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_4sswh2.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_5kj2k4.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_6w53db.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_7glv22.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_azkecq.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_be6wcg.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_by5cij.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_c33p5u.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_dkqzrn.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_dtzwof.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_eldtwl.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_euh4o4.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_evsh4b.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_fd5ohs.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_fhfxmf.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_fy4cla.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_g2ukou.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_g7yatv.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_h4f2qu.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_h6myna.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_hbc3re.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_hfihb2.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_i4qnsr.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_i7zvqf.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_idiknx.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_iev2ja.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_igd4qy.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_jc5co4.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_jdp35v.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_jfzhrq.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_jyeqlp.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_k4jaqg.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_lagezd.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_larfxh.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_ldblio.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_liamow.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_llz5d3.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_lnl5q7.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_mbzrx3.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_mnaa6u.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_mqmdo5.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_o424oh.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_ojas2g.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_owcucr.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_pdtbwe.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_pfqmzv.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_psb35r.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_qdw47i.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_spp6a3.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_suwt22.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_sz5zde.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_uuqhg2.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_uzjbsf.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_wounai.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_wtfxss.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_xubic3.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_xxdw6g.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_xzidwg.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_yeedmt.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_yesxmd.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_yhoxvo.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_z5de3t.enc
%{_texmfdistdir}/fonts/enc/dvips/ebgaramond/ebgm_zaj4rc.enc
%{_texmfdistdir}/fonts/map/dvips/ebgaramond/EBGaramond.map
%{_texmfdistdir}/fonts/opentype/public/ebgaramond/EBGaramond-Initials.otf
%{_texmfdistdir}/fonts/opentype/public/ebgaramond/EBGaramond12-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/ebgaramond/EBGaramond12-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramond12-Regular-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramondInitials-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramondInitials-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramondInitials-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramondInitials-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramondInitials-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/ebgaramond/EBGaramondInitials-tlf-ts1.tfm
%{_texmfdistdir}/fonts/truetype/public/ebgaramond/EBGaramond-Initials.ttf
%{_texmfdistdir}/fonts/truetype/public/ebgaramond/EBGaramond12-Italic.ttf
%{_texmfdistdir}/fonts/truetype/public/ebgaramond/EBGaramond12-Regular.ttf
%{_texmfdistdir}/fonts/type1/public/ebgaramond/EBGaramond12-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/ebgaramond/EBGaramond12-Regular.pfb
%{_texmfdistdir}/fonts/type1/public/ebgaramond/EBGaramondInitials.pfb
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-lf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-osf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tlf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tosf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-lf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-osf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tlf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tosf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramond12-Regular-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramondInitials-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramondInitials-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/ebgaramond/EBGaramondInitials-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/ebgaramond/LY1EBGaramond-LF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/LY1EBGaramond-OsF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/LY1EBGaramond-Sup.fd
%{_texmfdistdir}/tex/latex/ebgaramond/LY1EBGaramond-TLF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/LY1EBGaramond-TOsF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/LY1EBGaramondInitials-TLF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/OT1EBGaramond-LF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/OT1EBGaramond-OsF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/OT1EBGaramond-Sup.fd
%{_texmfdistdir}/tex/latex/ebgaramond/OT1EBGaramond-TLF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/OT1EBGaramond-TOsF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/OT1EBGaramondInitials-TLF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/T1EBGaramond-LF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/T1EBGaramond-OsF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/T1EBGaramond-Sup.fd
%{_texmfdistdir}/tex/latex/ebgaramond/T1EBGaramond-TLF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/T1EBGaramond-TOsF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/T1EBGaramondInitials-TLF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/TS1EBGaramond-LF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/TS1EBGaramond-OsF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/TS1EBGaramond-TLF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/TS1EBGaramond-TOsF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/TS1EBGaramondInitials-TLF.fd
%{_texmfdistdir}/tex/latex/ebgaramond/ebgaramond.sty
%{_texmfdistdir}/tex/latex/ebgaramond/mt-EBGaramond.cfg
%doc %{_texmfdistdir}/doc/fonts/ebgaramond/COPYING
%doc %{_texmfdistdir}/doc/fonts/ebgaramond/EBGaramond-Initials-Glyphs.pdf
%doc %{_texmfdistdir}/doc/fonts/ebgaramond/EBGaramond12-Italic-Glyphs.pdf
%doc %{_texmfdistdir}/doc/fonts/ebgaramond/EBGaramond12-Regular-Glyphs.pdf
%doc %{_texmfdistdir}/doc/fonts/ebgaramond/README
%doc %{_texmfdistdir}/doc/fonts/ebgaramond/Specimen.pdf
%doc %{_texmfdistdir}/doc/fonts/ebgaramond/samples.pdf
%doc %{_texmfdistdir}/doc/fonts/ebgaramond/samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}

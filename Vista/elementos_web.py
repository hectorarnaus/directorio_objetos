class ElementosWeb:
    @staticmethod
    def crea_parrafo(texto):
        return ('\t<!-- wp:paragraph -->\n'
            f'\t\t<p>{texto}</p>\n'
            '\t<!-- /wp:paragraph -->\n'
        )

    @staticmethod
    def crea_bloque_anuncio_manual():
        return (
            '<!-- wp:shortcode -->\n'
            '\t[adinserter name="anuncio_manual"]\n'
            '<!-- /wp:shortcode -->\n'
        )
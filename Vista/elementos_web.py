class ElementosWeb:
    @staticmethod
    def crea_parrafo(texto):
        res=('\t<!-- wp:paragraph -->\n'
            f'\t\t<p>{texto}</p>\n'
            '\t<!-- /wp:paragraph -->\n'
        )
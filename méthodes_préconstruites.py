try:
    from mot_clef import replace
    def add_méthodes(liste_replace:list[replace]) -> list[replace]:
        #A
        liste_replace.append(replace("__abs__", "__valeur_absolue__"))
        liste_replace.append(replace("__add__", "__addition__"))
        liste_replace.append(replace("__aenter__", "__async_entrée__"))
        liste_replace.append(replace("__aexit__", "__async_sortie__"))
        liste_replace.append(replace("__aiter__", "__async_itération__"))
        liste_replace.append(replace("__all__", "__tout__"))
        liste_replace.append(replace("__and__", "__et__"))
        liste_replace.append(replace("__anext__", "__async_suivant__"))
        liste_replace.append(replace("__annotations__", "__annotations__"))
        liste_replace.append(replace("__args__", "__arguments__"))
        liste_replace.append(replace("__await__", "__attendre__"))
        #B
        liste_replace.append(replace("__bases__", "__bases__"))
        liste_replace.append(replace("__bool__", "__booléen__"))
        liste_replace.append(replace("__breakpointhook__", "__crochet_de_point_d_arrêt__"))
        liste_replace.append(replace("__bytes__", "__octets__"))
        #C
        liste_replace.append(replace("__cached__", "__en_mémoire_cache__"))
        liste_replace.append(replace("__call__", "__appel__"))
        liste_replace.append(replace("__callback__", "__rappel__"))
        liste_replace.append(replace("__cause__", "__cause__"))
        liste_replace.append(replace("__ceil__", "__arrondir_par_excès__"))
        liste_replace.append(replace("__class__", "__classe__"))
        liste_replace.append(replace("__class_getitem__", "__obtenir_item_de_classe__"))
        liste_replace.append(replace("__classcell__", "__cellule_de_classe__"))
        liste_replace.append(replace("__closure__", "__fermeture__"))
        liste_replace.append(replace("__code__", "__code__"))
        liste_replace.append(replace("__complex__", "__complèxe__"))
        liste_replace.append(replace("__concat__", "__concaténation__"))
        liste_replace.append(replace("__contains__", "__contient__"))
        liste_replace.append(replace("__context__", "__contexte__"))
        liste_replace.append(replace("__copy__", "__copie__"))
        #D
        liste_replace.append(replace("__debug__", "__débogage__"))
        liste_replace.append(replace("__deepcopy__", "__copie_profonde__"))
        liste_replace.append(replace("__defaults__", "__défaut__"))
        liste_replace.append(replace("__del__", "__supp__"))
        liste_replace.append(replace("__delattr__", "__supprimer_attribut__"))
        liste_replace.append(replace("__delete__", "__supprimer__"))
        liste_replace.append(replace("__delitem__", "__supprimer_item__"))
        liste_replace.append(replace("__dict__", "__dictionnaire__"))
        liste_replace.append(replace("__dir__", "__dossier__"))
        liste_replace.append(replace("__displayhook__", "__affichage_crochet__"))
        liste_replace.append(replace("__divmod__", "__division_euclidienne_et_modulo__"))
        liste_replace.append(replace("__doc__", "__documentation__"))
        #E
        liste_replace.append(replace("__enter__", "__entrer__"))
        liste_replace.append(replace("__eq__", "__égal__"))
        liste_replace.append(replace("__excepthook__", "__rattraper_crochet__"))
        liste_replace.append(replace("__exit__", "__sortie__"))
        #F
        liste_replace.append(replace("__file__", "__fichier__"))
        liste_replace.append(replace("__float__", "__flottant__"))
        liste_replace.append(replace("__floor__", "__arrondir_par_défaut__"))
        liste_replace.append(replace("__floordiv__", "__division_euclidienne__"))
        liste_replace.append(replace("__format__", "__format__"))
        liste_replace.append(replace("__fspath__", "__chemin_fichiers_système__"))
        liste_replace.append(replace("__func__", "__fonction__"))
        liste_replace.append(replace("__future__", "__future__"))
        #G
        liste_replace.append(replace("_ge__", "__plus_grand_ou_égal__"))
        liste_replace.append(replace("__get__", "__obtenir__"))
        liste_replace.append(replace("__getattr__", "__obtenir_attribut_nommé__"))
        liste_replace.append(replace("__getattribute__", "__obtenir_attribut__"))
        liste_replace.append(replace("__getitem__", "__obtenir_item__"))
        liste_replace.append(replace("__getnewargs__", "__obtenir_nouveaux_arguments_arguments_non_positionnels_exclus__"))
        liste_replace.append(replace("__getnewargs_ex__", "__obtenir_nouveaux_arguments_arguments_non_positionnels_inclus__"))
        liste_replace.append(replace("__getstate__", "__obtenir_état__"))
        liste_replace.append(replace("__globals__", "__globales__"))
        liste_replace.append(replace("__gt__", "__strictement_plus_grand__"))
        #H
        liste_replace.append(replace("__hash__", "__découpage__"))
        #I
        liste_replace.append(replace("__iadd__", "__addition_sur_place__"))
        liste_replace.append(replace("__iand__", "__et_sur_place__"))
        liste_replace.append(replace("__iconcat__", "__concaténation_sur_place__"))
        liste_replace.append(replace("__ifloordir__", "__division_euclidienne_sur_place__"))
        liste_replace.append(replace("__ilshift__", "__décalage_vers_la_gauche_sur_place__"))
        liste_replace.append(replace("__imatmul__", "__multiplication_matrice_sur_place__"))
        liste_replace.append(replace("__imod__", "__modulo_sur_place__"))
        liste_replace.append(replace("__import__", "__importation__"))
        liste_replace.append(replace("__imul__", "__multiplication_sur_place__"))
        liste_replace.append(replace("__index__", "__index__"))
        liste_replace.append(replace("__init__", "__initialisation__"))
        liste_replace.append(replace("__init_subclass__", "__initialisation_sous_classe__"))
        liste_replace.append(replace("__instancecheck__", "__vérification_instance__"))
        liste_replace.append(replace("__int__", "__entier__"))
        liste_replace.append(replace("__interactivehook__", "__crochet_intéractif__"))
        liste_replace.append(replace("__inv__", "__inv__"))
        liste_replace.append(replace("__invert__", "__inverser__"))
        liste_replace.append(replace("__ior__", "__ou_sur_place__"))
        liste_replace.append(replace("__ipow__", "__puissance_sur_place__"))
        liste_replace.append(replace("__irshift__", "__décalage_vers_la_droite_sur_place__"))
        liste_replace.append(replace("__isub__", "__soustraction_sur_place__"))
        liste_replace.append(replace("__iter__", "__itération__"))
        liste_replace.append(replace("__itruediv__", "__vraie_division_sur_place__"))
        liste_replace.append(replace("__ixor__", "__xou_sur_place__"))
        #K
        liste_replace.append(replace("__kwdefaults__", "__dictionnaire_paramètre_mot_clef__"))
        #L
        liste_replace.append(replace("__le__", "__plus_petit_ou_égal__"))
        liste_replace.append(replace("__len__", "__longueur__"))
        liste_replace.append(replace("__length_hint__", "__taille_estimée__"))
        liste_replace.append(replace("__loader__", "__chargeur__"))
        liste_replace.append(replace("__lshift__", "__décalage_vers_la_gauche__"))
        liste_replace.append(replace("__lt__", "__strictement_plus_petit__"))
        #M
        liste_replace.append(replace("__main__", "__principal__"))
        liste_replace.append(replace("__matmul__", "__multiplication_matrice__"))
        liste_replace.append(replace("__missing__", "__manquant__"))
        liste_replace.append(replace("__mod__", "__modulo__"))
        liste_replace.append(replace("__module__", "__module__"))
        liste_replace.append(replace("__mro__", "__méthode_résolution_objet__"))
        liste_replace.append(replace("__mro_entries__", "__entrées_méthode_résolution_objet__"))
        liste_replace.append(replace("__mul__", "__multiplication__"))
        #N
        liste_replace.append(replace("__name__", "__nom__"))
        liste_replace.append(replace("__ne__", "__différent__"))
        liste_replace.append(replace("__neg__", "__opposé__"))
        liste_replace.append(replace("__new__", "__nouveau__"))
        liste_replace.append(replace("__next__", "__suivant__"))
        liste_replace.append(replace("__not__", "__non__"))
        liste_replace.append(replace("__notes__", "__notes__"))
        #O
        liste_replace.append(replace("__optional_keys__", "__clés_optionnelles__"))
        liste_replace.append(replace("__or__", "__ou__"))
        liste_replace.append(replace("__origin__", "__origine__"))
        #P
        liste_replace.append(replace("__package__", "__packets__"))
        liste_replace.append(replace("__parameters__", "__paramètres__"))
        liste_replace.append(replace("__path__", "__chemin__"))
        liste_replace.append(replace("__pos__", "__position__"))
        liste_replace.append(replace("__pow__", "__puissance__"))
        liste_replace.append(replace("__prepare__", "__préparer__"))
        liste_replace.append(replace("__PYVENV_LAUNCHER__", "__LANCEUR_ENVIRONNEMENT_VIRTUEL_PYTHON__"))
        #Q
        liste_replace.append(replace("__qualname__", "__nom_qualifié__"))
        #R
        liste_replace.append(replace("__radd__", "__addition_reflétée__"))
        liste_replace.append(replace("__rand__", "__et_reflété__"))
        liste_replace.append(replace("__rdivmod__", "__division_euclidienne_et_modulo_reflétée__"))
        liste_replace.append(replace("__reduce__", "__réduire_argument_exclus__"))
        liste_replace.append(replace("__reduce_ex__", "__réduire_argument_inclus__"))
        liste_replace.append(replace("__repr__", "__représentation__"))
        liste_replace.append(replace("__required_keys__", "__clefs_nécessaires__"))
        liste_replace.append(replace("__reversed__", "__renversé__"))
        liste_replace.append(replace("__rfloordiv__", "__division_euclidienne_reflétée__"))
        liste_replace.append(replace("__rlshift__", "__décalage_vers_la_gauche_reflété__"))
        liste_replace.append(replace("__rmatmul__", "__multiplication_matrice_reflétée__"))
        liste_replace.append(replace("__rmod__", "__modulo_reflété__"))
        liste_replace.append(replace("__ror__", "__ou_reflété__"))
        liste_replace.append(replace("__round__", "__arrondir__"))
        liste_replace.append(replace("__rpow__", "__puissance_reflétée__"))
        liste_replace.append(replace("__rrshift__", "__décalage_vers_la_droite_reflété__"))
        liste_replace.append(replace("__rshift__", "__décalage_vers_la_droite__"))
        liste_replace.append(replace("__rsub__", "__soustraction_reflétée__"))
        liste_replace.append(replace("__rtruediv__", "__vraie_division_reflétée__"))
        liste_replace.append(replace("__rxor__", "__xou_reflété__"))
        #S
        liste_replace.append(replace("__self__", "__soit__"))
        liste_replace.append(replace("__set__", "__mettre__"))
        liste_replace.append(replace("__set_name__", "__mettre_le_nom__"))
        liste_replace.append(replace("__setattr__", "__mettre_attribut__"))
        liste_replace.append(replace("__setitem__", "__mettre_item__"))
        liste_replace.append(replace("__setstate__", "__mettre_état__"))
        liste_replace.append(replace("__slots__", "__cases__"))
        liste_replace.append(replace("__spec__", "__spécifications__"))
        liste_replace.append(replace("__stderr__", "__sortie_erreur__"))
        liste_replace.append(replace("__stdin__", "__entrée_standard__"))
        liste_replace.append(replace("__stdout__", "__sortie_standard__"))
        liste_replace.append(replace("__str__", "__chaîne_de_charactères__"))
        liste_replace.append(replace("__sub__", "__soustraction__"))
        liste_replace.append(replace("__subclasscheck__", "__vérification_sous_classe__"))
        liste_replace.append(replace("__subclasses__", "__sous_classes__"))
        liste_replace.append(replace("__subclasshook__", "__crochet_sous_classe__"))
        liste_replace.append(replace("__suppress_context__", "__suppression_contexte__"))
        #T
        liste_replace.append(replace("__total__", "__total__"))
        liste_replace.append(replace("__traceback__", "__retour__"))
        liste_replace.append(replace("__truediv__", "__vraie_division__"))
        liste_replace.append(replace("__trunc__", "__tronquer__"))
        #U
        liste_replace.append(replace("__unpacked__", "__dépaqueté__"))
        liste_replace.append(replace("__unraisablehook__", "__crochet_non_remontable__"))
        #X
        liste_replace.append(replace("__xor__", "__xou__"))
        return liste_replace
except ModuleNotFoundError:
    def add_méthodes(liste_replace:list) -> list:
        import sys
        print("Méthodes non chargées", file=sys.stderr)
        return liste_replace

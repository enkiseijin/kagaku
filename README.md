## メディア情報学特論

---

1.データセットの準備
MNISTのデータセットのうち100件(クラスごとに10件)を画像化
参考URL:https://qiita.com/kaityo256/items/77bc0b40e3bb70d36f3d

---

memo

参考URL:https://qiita.com/best_not_best/items/c9497ffb5240622ede01


matches = bf.match(des1,des2) と書いてある行の結果はDMatch型オブジェクトのリストが返ってきます．このDMatch型オブジェクトとは以下のような属性を持っています:

DMatch.distance - 特徴量記述子間の距離．低いほど良い．
DMatch.trainIdx - 学習記述子(参照データ)中の記述子のインデックス．
DMatch.queryIdx - クエリ記述子(検索データ)中の記述子のインデックス．
DMatch.imgIdx - 学習画像のインデックス．


dictionalyに[ファイル名][BFMatcherの距離]を入れて要素でそーと，表示する→検索

# pylogger

A logger for Python projects.

## 開発

### 準備

依存関係の解決などもpoetryによって行っているのでインストールする．
また，必要なバージョンをインストールできるようにpyenvもインストールしておく．

#### ローカルにて必要なものをインストール

```shell
pip install poetry

# 依存関係のインストール
poetry install

# 仮想環境初期化
poetry shell

# コミット前の確認スクリプトをインストール
pre-commit install
```

#### Dockerを使わない場合の環境構築

以下のコマンドで依存関係を解消する．

```shell
poetry install
```

#### Docker

##### 前提となる環境

* Dockerクライアントがホストマシンにインストールされていること

##### macOS での Docker セットアップ

以下のコマンドを実行後，Docker.appを起動し，`docker ps`等にてインストールの確認．

```bash
# docker-compose も導入されるはず
brew cask install docker
```

##### コンテナの立ち上げ

以下のコマンドでDockerコンテナが立ち上がる．

```shell
make run
```

成功すれば，`docker ps`でコンテナが起動していることが確認できるはず．

***

#### Test

```shell
make test

# OR

poetry run test
```

***

#### Linter

```shell
make lint

# OR

poetry run lint
```

自動で修正する場合は以下のコマンドを実行する．

```shell
make format

# OR

poetry run format
```

***

#### Debug

以下のコマンドが利用可能．詳細は[Makefile](./Makefile)を参照のこと．

```shell
make enter      # コンテナに入る
make log        # ログを見始める
```

***

#### CI

GitHub Actionsのconfigを[`.github/workflows`](./.github/workflows)に記述している．現在は以下の設定になっている．

* すべてのcommitに対してtestが走る．
* releaseへのcommitに対して，`release/{date}_{number}`タグが切られる．

このため，基本的には`dev`ブランチを切って，それをdefaultブランチに設定し，`release`へのcommitは`dev`ブランチのマージによって行うと良い．

***

## ディレクトリ構成

```shell
.
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── coverage.xml
├── docker-compose.yml
├── main.py
├── poetry.lock
├── pylogger
├── pyproject.toml
├── pytest.log
├── rename_me
├── samples
├── setup.cfg
├── setup.py
└── tests
```

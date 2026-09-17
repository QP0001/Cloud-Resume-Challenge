# Cloud Resume Challenge - AWS

**19歳・高卒・AWS SAA取得者**が、プログラミング経験ゼロから挑戦したクラウドポートフォリオです。

**🌐 公開URL**：https://d3819481cvuung.cloudfront.net

---

## これは何？

自分の履歴書をAWS上で公開し、**ページを開いた人の数を自動でカウント・表示**する仕組みを作りました。

アクセスすると、画面の下に **「Visitors: ○○」** と表示されます。これはAWS上で動くプログラムがリアルタイムでカウントしています。

---

## システム構成

1. **S3** に履歴書（HTML/CSS/JavaScript）を保存
2. **CloudFront** でHTTPS化し、世界中から高速にアクセスできるように配信
3. **API Gateway** が「訪問者数を教えて」とのリクエストを受け付ける入口に
4. **Lambda（Python）** が「訪問者数を1増やして返す」処理を実行
5. **DynamoDB** が訪問者数のデータを永続保存
6. **Terraform** で上記のAWSリソースをコード化し、再現性を担保
7. **GitHub Actions** でコードをPushするだけで自動テスト・自動デプロイ

## 使用技術

| 役割 | 技術 |
|---|---|
| 履歴書ページ | HTML / CSS / JavaScript |
| カウンター処理 | Python (boto3) |
| ページ公開 | S3 + CloudFront (HTTPS) |
| カウンターAPI | API Gateway + Lambda |
| データ保存 | DynamoDB |
| インフラ管理 | Terraform |
| 自動デプロイ | GitHub Actions |
| テスト | pytest + moto |

---

## 実装したこと

### 1. サーバーレスな訪問者カウンター
- ページを開くたびに、AWS Lambda（Python）がDynamoDBの数字を+1して画面に返す

### 2. Infrastructure as Code（IaC）
- DynamoDB・Lambda・API Gateway を **Terraform** でコード化
- 「ボタンをポチポチ押して作る」ではなく、「コードを実行すれば同じ環境が作れる」状態にした

### 3. CI/CD（自動デプロイ）
- **フロントエンド**：HTMLを修正してPushするだけで、自動的にS3にアップロード＋CloudFrontキャッシュクリア
- **バックエンド**：PythonコードをPushするだけで、自動テスト → Lambda関数の更新まで実行

---

## 躓いたことと解決法

| 困ったこと | どう解決したか |
|---|---|
| API GatewayでCORSエラーが出た | CORS設定の保存とステージのデプロイを徹底して実施 |
| GitHub ActionsでAWS認証エラー | Secretsの値を確認し、正しい認証情報を再登録 |
| テスト実行時にリージョンエラー | boto3の設定にリージョンを明示的に指定して解決 |

---

## 資格

- **AWS Certified Solutions Architect – Associate**（2026年9月取得）

---

## 今後の展開

このプロジェクトは「練習台」として位置づけています。2026年10月下半期から、**本番アプリ（WordPress on ECS Fargate + RDS MySQL）**の構築・運用に移行し、半年以上の運用実績（監視・障害対応・コスト最適化・バックアップテスト）を就活時に提示することを目標としています。

---

## 学んだこと

- **インフラエンジニアに、ゼロからコードを書く必要はない**。既存のコードを読み・借り・組み合わせる力が大切。
- **Terraform** を使うことで、手動設定の記憶に頼らず、インフラを再現・管理できる。
- **CI/CD** を整備することで、デプロイの手間とヒューマンエラーを大幅に削減できる。
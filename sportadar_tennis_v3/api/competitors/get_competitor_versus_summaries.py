from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_competitor_versus_summaries_locale import GetCompetitorVersusSummariesLocale
from ...types import Response


def _get_kwargs(
    locale: GetCompetitorVersusSummariesLocale,
    urn_competitor: str,
    urn_competitor2: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/competitors/{urn_competitor}/versus/{urn_competitor2}/summaries",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetCompetitorVersusSummariesLocale,
    urn_competitor: str,
    urn_competitor2: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """list last 10 results and the next 10 schedules for a competitor against another competitor

     List last 10 results and the next 10 schedules for a competitor against another competitor.

    Args:
        locale (GetCompetitorVersusSummariesLocale):
        urn_competitor (str):
        urn_competitor2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        urn_competitor=urn_competitor,
        urn_competitor2=urn_competitor2,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    locale: GetCompetitorVersusSummariesLocale,
    urn_competitor: str,
    urn_competitor2: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """list last 10 results and the next 10 schedules for a competitor against another competitor

     List last 10 results and the next 10 schedules for a competitor against another competitor.

    Args:
        locale (GetCompetitorVersusSummariesLocale):
        urn_competitor (str):
        urn_competitor2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
        urn_competitor=urn_competitor,
        urn_competitor2=urn_competitor2,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
